from ..constants import CARDS_METAFILE
from ..card_data.cards_getter import CardsGetter
from ..elo_data.elocards_getter import ElocardsGetter

class CardsParser :

    TYPES_SEPARATOR = ' '
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
                color=[c for c in color.strip()],
                mana_value=int(manavalue.strip()),
                card_types=[sub.strip() for sub in types.split(cls.TYPES_SEPARATOR) if sub.strip()],
            )

            ElocardsGetter.add_card_to_database_from_data(
                card_id=CardsGetter.get_card_from_name(card_name=cardname.strip()).id,
            )

        CardsGetter.save_database()
        ElocardsGetter.save_database()
        
        # Delete metafile
        with open(CARDS_METAFILE, 'w') as cards_metafile:
            pass


