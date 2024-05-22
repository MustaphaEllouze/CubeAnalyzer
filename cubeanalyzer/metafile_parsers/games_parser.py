from ..constants import GAMES_METAFILE
from ..game_data.games_register import GamesRegister

class GamesParser:

    DATA_SEPARATOR = '/'

    @classmethod
    def parse_metafile(cls, )->None:
        with open(GAMES_METAFILE, 'r') as games_metafile:
            data = games_metafile.readlines()
        
        for line in data :
            if line.strip() == '' : continue
            if not 'game' in line : 
                raise ValueError(f'Invalid syntax of games metafile.')
            (
                _,
                deck1_id,
                deck2_id,
                d1_wins,
                d2_wins,
            ) = line.split(cls.DATA_SEPARATOR)

            GamesRegister.register_new_game(
                deck1_id=int(deck1_id),
                deck2_id=int(deck2_id),
                deck1_wins=int(d1_wins),
                deck2_wins=int(d2_wins),
            )

        GamesRegister.save_database()

        # Delete the metafile once parsed
        with open(GAMES_METAFILE, 'w') : pass