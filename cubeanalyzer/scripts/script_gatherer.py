from ..metafile_parsers.cards_parser import CardsParser
from ..metafile_parsers.decks_parser import DecksParser
from ..card_data.cards_getter import CardsGetter
from ..game_data.games_runner import GamesRunner
from ..elo_data.elo_modifier import EloModifier

class ScriptGatherer:

    @classmethod
    def parse_card_metafile(cls, )->None:
        CardsParser.parse_metafile()
    
    @classmethod
    def parse_deck_metafile(cls, )->None:
        DecksParser.parse_metafile()
    
    @classmethod
    def print_possible_card_matches(cls, string_to_match:str)->None:
        possible_matches = tuple(
            c
            for c in CardsGetter.get_all_cards()
            if string_to_match.lower() in c.name.lower()
        )
        print(f'{len(possible_matches)} possible matches for "{string_to_match}"')
        for pm in possible_matches:
            print(f'    | {pm.name} | ID = {pm.id}')
    
    @classmethod
    def compile_game_results(cls, )->None:
        GamesRunner.run_all_games()
        EloModifier.set_elo_distribution()
        EloModifier.update_json_elo_cards()
