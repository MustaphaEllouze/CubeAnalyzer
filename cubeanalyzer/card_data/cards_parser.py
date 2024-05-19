from ..constants import CARDS_METAFILE, CARDS_DATA_JSON_FILE
from ..elo_model.elo import EloTracker
from ..card_data.cards_getter import CardsGetter

class CardsParser :

    TYPES_SEPARATOR = ','
    DATA_SEPARATOR = '/'

    @classmethod
    def parse_metafile(cls, ):

        with open(CARDS_METAFILE, 'r') as cards_metafile:
            content = cards_metafile.readlines()
        
        for card in content :
            stripped_card = card.strip()
            if stripped_card == '' : continue
            splitted_data = stripped_card.split(cls.DATA_SEPARATOR)
            if not len(splitted_data) == 4 :
                raise ValueError(f'Invalid line: {stripped_card}')
            cardname, color, manavalue, types = splitted_data
            if not manavalue.strip().isdigit() : 
                raise ValueError(f'Invalid mana value: {manavalue}')
            CardsGetter.add_card_to_database_from_data(
                name=cardname.strip(),
                color=color.strip(),
                mana_value=int(manavalue.strip()),
                card_types=[sub.strip() for sub in types.split(cls.TYPES_SEPARATOR)],
            )
            CardsGetter.save_database()
        
        # Delete metafile
        with open(CARDS_METAFILE, 'w') as cards_metafile:
            pass


