from typing import Tuple

from arena_data.utils import *


def new_cards(card_path: Path, loc_path: Path, sql_path: Path, new_set_code: str, old_set_codes: Set[str]) -> Set[
    Tuple[str]]:
    """
    Finds cards in the Arena data files that aren't in a list of sets we would expect
    :param card_path: Path to the cards Arena data file
    :param loc_path: Path to the loc Arena data file
    :param sql_path: Path to the MTGSQLive database
    :param new_set_code: The set code of interest, e.g. AKR (Amonkhet Remastered)
    :param old_set_codes: The old sets that the new set is based on, e.g. for AKR these would be AKH and HOU
    """
    lookup = read_loc(loc_path)
    conn = connect_sql(sql_path)
    cursor = conn.cursor()
    old_cards = list_cards_in_set(cursor, old_set_codes)
    new = set()

    with card_path.open() as fp:
        parsed = json.load(fp)

    for card in parsed:
        if card['set'] == new_set_code and not card['isToken']:
            card_name = lookup[card['titleId']].replace('///', '//')
            if card_name not in old_cards:
                # If we didn't find an art by this artist, it's probably new
                new.add((card_name,))

    return new


def new_arts(card_path: Path, loc_path: Path, sql_path: Path, set_code: str = None) -> Set[Tuple[str, str]]:
    """
    Finds cards in the Arena data files that aren't yet in MTGJSON
    :param card_path: Path to the cards Arena data file
    :param loc_path: Path to the loc Arena data file
    :param sql_path: Path to the MTGSQLive database
    :param set_code: Optionally, a set to filter results to, e.g. AKR
    """
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
