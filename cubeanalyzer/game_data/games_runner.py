import json

from ..constants import GAMES_JSON_FILE
from ..game_model.game import Game
from ..elo_data.elodecks_getter import ElodecksGetter

class GamesRunner :

    @classmethod
    def read_games(cls, )->tuple[dict[str, int]]:
        with open(GAMES_JSON_FILE) as json_file:
            data = json.load(json_file)['games']
        
        return data

    @classmethod
    def run_all_games(cls, )->None:
        games_as_json = GamesRunner.read_games()

        for g in games_as_json :
            Game.register_game(
                deck1=ElodecksGetter.get_elo_deck_from_id(
                    deck_id=g.get('deck1_id', None)
                ),
                deck2=ElodecksGetter.get_elo_deck_from_id(
                    deck_id=g.get('deck2_id', None)
                ),
                deck1_wins=g.get('deck1_wins', None),
                deck2_wins=g.get('deck2_wins'),
            )