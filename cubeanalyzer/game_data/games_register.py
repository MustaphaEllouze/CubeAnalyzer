import json

from ..constants import GAMES_JSON_FILE
from ..elo_model.elo_deck import EloDeck
from ..elo_data.elodecks_getter import ElodecksGetter
from ..game_model.game import Game
from .games_runner import GamesRunner

class GamesRegister:

    GAMES = GamesRunner.read_games()

    @classmethod
    def register_new_game(
        cls,
        deck1_id:int,
        deck2_id:int,
        deck1_wins:int,
        deck2_wins:int,
    )->None:
        cls.GAMES += (
            Game(
                deck1=ElodecksGetter.get_elo_deck_from_id(deck_id=deck1_id),
                deck2=ElodecksGetter.get_elo_deck_from_id(deck_id=deck2_id),
                deck1_wins=deck1_wins,
                deck2_wins=deck2_wins,
            ).to_json()
        )
    
    @classmethod
    def save_database(cls, )->None:
        with open(GAMES_JSON_FILE, 'r') as database:
            json.dump(
                cls.GAMES,
                database,
                indent=4,
            )