# Cube Analyzer

Set of tools to analyze the performance of single cards and draw statistics for your Mtg Cube.

## How to add cards in the database ?
* You should first add the relevant info in the **cards metafile**, following this syntax (if the card has several types, they should be separated by a comma) :
```
NAME OF THE CARD / COLOR / MANA VALUE / TYPES
```
* Then, run the script with 
```
python3 cubeanalyzer_scripts.py -c
```
* Data that you gave will be consumed and interpreted, and the cards will be added to the database. **Note** : the metafile will be emptied.

## Syntax
```
/deck/
CARD 1
CARD 2
...
```

## TODO
* [ ] Add way to visualize the data simply
* [ ] Add data-processing functions (ELO per type, per mv etc.)