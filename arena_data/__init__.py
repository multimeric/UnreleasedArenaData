from pathlib import Path
import json
import scrython
from typing import Set, Dict, Optional
import sqlite3
from collections import defaultdict
import unicodedata

def new_arts(card_path: Path, loc_path: Path, sql_path: Path, set_code: str = None) -> Set[str]:
    lookup = read_loc(loc_path)
    conn = connect_sql(sql_path)
    cursor = conn.cursor()
    all_arts = list_all_arts(cursor)

    new = set()
    with card_path.open() as fp:
        parsed = json.load(fp)
    for card in parsed:

        # If requested, skip other sets
        if set_code is not None and card['set'] != set_code:
            continue

        card_name = lookup[card['titleId']]
        artist = to_ascii(card['artistCredit'])

        if card_name in all_arts:
            if artist not in all_arts[card_name]:
                # If we didn't find an art by this artist, it's probably new
                new.add((card_name, card['artistCredit']))

    return new