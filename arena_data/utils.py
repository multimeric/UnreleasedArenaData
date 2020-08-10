from pathlib import Path
import json
from typing import Set, Dict, Optional, Sized, Sequence
import sqlite3
from collections import defaultdict
import unicodedata

def read_loc(loc_file: Path, language='en-US') -> Dict[int, str]:
    """
    Builds a dictionary that maps from localisation IDs to strings
    :param loc_file: Path to the loc file
    :param language: The language of interest
    """
    ret = {}
    with loc_file.open() as fp:
        for lang in json.load(fp):
            if lang['isoCode'] != language:
                # Skip languages we don't want
                continue
            for entry in lang['keys']:
                ret[entry['id']] = entry['text']
            break

    return ret


def connect_sql(sql_path: Path) -> sqlite3.Connection:
    return sqlite3.connect(str(sql_path))


def to_ascii(s: str) -> Optional[str]:
    if s is None:
        return s
    else:
        return unicodedata.normalize('NFD', s).encode('ascii', 'ignore').lower()


def list_all_arts(sql_cur: sqlite3.Cursor, tokens=True) -> Dict[str, Set[str]]:
    """
    Returns a dictionary mapping card_name to a set of artist_name
    :param tokens: If true, include tokens
    """
    ret = defaultdict(set)
    for row in sql_cur.execute('SELECT DISTINCT faceName, name, artist FROM cards'):
        name = row[0] or row[1]
        ret[name].add(to_ascii(row[2]))

    if tokens:
        for row in sql_cur.execute('SELECT DISTINCT faceName, name, artist FROM tokens'):
            name = row[0] or row[1]
            ret[name].add(to_ascii(row[2]))

    return dict(ret)


def list_cards_in_set(sql_cur: sqlite3.Cursor, sets: Sequence[str]) -> Set[str]:
    """
    Returns a set of cardnames in a group of sets
    """
    ret = set()
    set_placeholders = ', '.join(['?'] * len(sets))
    query = 'SELECT DISTINCT faceName, name FROM cards WHERE cards.setCode IN ({})'.format(set_placeholders)
    for row in sql_cur.execute(query, list(sets)):
        ret.update([name for name in row if name])

    return ret


