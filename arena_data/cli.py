import argparse
from arena_data import new_arts
from pathlib import Path
from typing import Iterable, Tuple


def print_tuples(iterable: Iterable[Tuple]):
    print('\n'.join([','.join(tup) for tup in iterable]))


def get_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description='Calculates interesting trivia from the MTG Arena data files')
    subparsers = parser.add_subparsers()

    new_art_cmd = subparsers.add_parser('new-art', help='Finds cards with new, unreleased art')
    new_art_cmd.add_argument('card_path', type=Path, help='Path to the card data file')
    new_art_cmd.add_argument('--loc-path', type=Path, help='Path to the localisation data file')
    new_art_cmd.add_argument('--sql-path', type=Path,
                             help='Path to MTGJSON AllPrintings SQL database, e.g. https://mtgjson.com/api/v5/AllPrintings.sql')
    new_art_cmd.add_argument('--set-code', help='Optionally, a set code to restrict the search to, e.g. "AKR" (Amonkhet Remastered)')
    new_art_cmd.set_defaults(func=lambda **kwargs: print_tuples(new_arts(**kwargs)))

    return parser


def main():
    parser = get_parser()
    args = vars(parser.parse_args())
    func = args.pop('func')
    func(**args)


if __name__ == '__main__':
    main()
