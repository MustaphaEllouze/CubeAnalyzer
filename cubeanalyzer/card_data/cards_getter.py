from ..constants import CARDS_DATA_JSON_FILE
from ..card_model.card import Card
from .cards_constructor import CardsConstructor

class CardsGetter :
    CARDS = CardsConstructor.contruct_cards(
        json_data=CARDS_DATA_JSON_FILE,
    )

    # Check that there is unique IDs
    __check_id_list = []
    for c in CARDS :
        if c.id in __check_id_list : 
            raise ValueError(f'{c.name} uses an already taken id.')
        __check_id_list.append(c.id)

    CARDS_FROM_NAME = {
        c.name:c
        for c in CARDS
    }

    CARDS_FROM_ID = {
        c.id:c
        for c in CARDS
    }

    @classmethod
    def get_card_from_name(
        cls,
        card_name:str,
    )->Card:
        return CardsGetter.CARDS_FROM_NAME.get(card_name, None)
    
    @classmethod
    def get_card_from_id(
        cls,
        card_id : int,

    )->Card:
        if not card_id in CardsGetter.CARDS_FROM_ID : 
            raise ValueError(f'Card with ID {card_id} does not exist.')
        return CardsGetter.CARDS_FROM_ID.get(card_id, None)