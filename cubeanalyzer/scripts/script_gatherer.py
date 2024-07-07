from ..metafile_parsers.cards_parser import CardsParser
from ..metafile_parsers.decks_parser import DecksParser
from ..metafile_parsers.games_parser import GamesParser
from ..card_data.cards_getter import CardsGetter
from ..game_data.games_runner import GamesRunner
from ..elo_data.elo_modifier import EloModifier
from ..elo_data.elocards_getter import ElocardsGetter

class ScriptGatherer:

    @classmethod
    def parse_card_metafile(cls, )->None:
        CardsParser.parse_metafile()
    
    @classmethod
    def parse_deck_metafile(cls, )->None:
        DecksParser.parse_metafile()
    
    @classmethod
    def parse_game_metafile(cls, )->None:
        GamesParser.parse_metafile()
    
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
    def run_game_results(cls, )->None:
        GamesRunner.run_all_games()
    
    @classmethod
    def update_json_elo_cards(cls, )->None:
        EloModifier.update_json_elo_cards()
    
    @classmethod
    def print_best_elo_cards(cls, number:int)->None:
        elo_cards = ElocardsGetter.get_all_cards()
        
        sorted_elo_cards = sorted(
            elo_cards,
            key=lambda c : c.elo,
            reverse = number>0
        )
        
        print(
            f'{"Best" if number > 0 else "Worse"} {abs(number)} cards sorted by elo'
        )

        for sec in sorted_elo_cards[:abs(number)]:
            print(f'    | {sec.name} | ELO = {sec.elo}')
