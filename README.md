# Arena Data
This is a set of simple command-line utilities for analysing the Magic: the Gathering Arena data files, to determine interesting trivia.

To use this package you'll need basic command-line skills, and have Python 3 installed.

## Installation
Setup a virtual environment with Python 3, then:

```bash
pip install git+https://github.com/TMiguelT/UnreleasedArenaData.git
```

## Usage
### Requirements
To use the below commands, you'll first have to locate your MTG Arena data directory. On Windows, this is something like `C:/Program Files/Wizards of the Coast/MTGA/MTGA_Data/Downloads/Data`. 

If a command below requires the input of a data file such as the `loc-path`, look in this directory for the newest file that begins with `data_loc_*.mtga`. Note: *don't* choose the `.mtga.dat` file, this is different. Similarly, the `card_path` will be named something like `data_cards_*.mtga`.

Secondly, you'll need a copy of the MTGSQLive database. You can download it [here](https://mtgjson.com/api/v5/AllPrintings.sql).

### New Arts
```
usage: Calculates interesting trivia from the MTG Arena data files new-art
       [-h] [--loc-path LOC_PATH] [--sql-path SQL_PATH] [--set-code SET_CODE]
       card_path
Calculates interesting trivia from the MTG Arena data files new-art: error: the following arguments are required: card_path
```


