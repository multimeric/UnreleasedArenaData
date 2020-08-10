# Arena Data
This is a set of simple command-line utilities for analysing the Magic: the Gathering Arena data files, to determine interesting trivia.

To use this package you'll need basic command-line skills, and have Python 3 installed.

## Installation
Setup a virtual environment with Python 3, then:

```bash
pip install git+https://github.com/TMiguelT/UnreleasedArenaData.git
```

### Requirements
To use the below commands, you'll first have to locate your MTG Arena data directory. On Windows, this is something like `C:/Program Files/Wizards of the Coast/MTGA/MTGA_Data/Downloads/Data`. 

If a command below requires the input of a data file such as the `loc-path`, look in this directory for the newest file that begins with `data_loc_*.mtga`. Note: *don't* choose the `.mtga.dat` file, this is different. Similarly, the `card_path` will be named something like `data_cards_*.mtga`.

Secondly, you'll need a copy of the MTGSQLive database. You can download it [here](https://mtgjson.com/api/v5/AllPrintings.sql).


## Usage
### New Arts
Finds art credits in the Arena data files that aren't yet in MTGJSON
```
usage: arena-data new-art [-h] [--loc-path LOC_PATH] [--sql-path SQL_PATH]
                          [--set-code SET_CODE]
                          card_path

positional arguments:
  card_path            Path to the card data file

optional arguments:
  -h, --help           show this help message and exit
  --loc-path LOC_PATH  Path to the localisation data file
  --sql-path SQL_PATH  Path to MTGJSON AllPrintings SQL database, e.g.
                       https://mtgjson.com/api/v5/AllPrintings.sql
  --set-code SET_CODE  Optionally, a set code to restrict the search to, e.g.
                       "AKR" (Amonkhet Remastered)
```

### New Cards
Finds cards in the Arena data files that aren't yet in MTGJSON
```
usage: arena-data new-cards [-h] [--loc-path LOC_PATH] [--sql-path SQL_PATH]
                            [--new-set-code NEW_SET_CODE]
                            [--old-set-codes OLD_SET_CODES]
                            card_path

positional arguments:
  card_path             Path to the card data file

optional arguments:
  -h, --help            show this help message and exit
  --loc-path LOC_PATH   Path to the localisation data file
  --sql-path SQL_PATH   Path to MTGJSON AllPrintings SQL database, e.g.
                        https://mtgjson.com/api/v5/AllPrintings.sql
  --new-set-code NEW_SET_CODE
                        The set code of interest, e.g. `AKR` (Amonkhet
                        Remastered)
  --old-set-codes OLD_SET_CODES
                        The old sets that the new set is based on as a comma-
                        separated list, e.g. for AKR this should be `AKH,HOU`
```
