import json

CARDS_DATA_JSON_FILE = './cubeanalyzer/card_data/data.json'
DECK_DATA_JSON_FILE = './cubeanalyzer/deck_data/data.json'
CARD_ELO_JSON_FILE = './cubeanalyzer/elo_data/data.json'
CARD_ELO_COMPILED_JSON_FILE = './cubeanalyzer/elo_data/data_compiled.json'
GAMES_JSON_FILE = './cubeanalyzer/game_data/data.json'

with open('./config.json') as json_config:
    config_data = json.load(json_config)

CARDS_METAFILE = config_data['cards_metafile']
DECKS_METAFILE = config_data['decks_metafile']