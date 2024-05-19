import json
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
        c.name.capitalize():c
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
        return CardsGetter.CARDS_FROM_NAME.get(card_name.capitalize(), None)
    
    @classmethod
    def get_card_from_id(
        cls,
        card_id : int,

    )->Card:
        if not card_id in CardsGetter.CARDS_FROM_ID : 
            raise ValueError(f'Card with ID {card_id} does not exist.')
        return CardsGetter.CARDS_FROM_ID.get(card_id, None)
    
    @classmethod
    def get_all_cards(cls, )->tuple[Card]:
        return cls.CARDS
    
    @classmethod
    def add_card_to_database_from_data(
        cls,
        name:str,
        color:str,
        mana_value:int,
        card_types:tuple[str],
    )->None:
        max_id = max([c.id for c in cls.CARDS])
        new_card = Card.from_data(
            name=name,
            color=color,
            mana_value=mana_value,
            card_types=card_types,
            id = max_id + 1,
        )
        cls.add_card_to_database(card=new_card)
    
    @classmethod
    def add_card_to_database(cls, card:Card)->None:
        if card.id in cls.CARDS_FROM_ID : 
            raise ValueError(f'Card ID {card.id} is already taken.')
        cls.CARDS += (card, )
        cls.CARDS_FROM_ID[card.id] = card
        cls.CARDS_FROM_NAME[card.name.capitailze()] = card
    
    @classmethod
    def save_database(cls, )->None:
        with open(CARDS_DATA_JSON_FILE, 'w') as json_data_cards :
            json.dump(
                {"cards" : [c.to_json() for c in cls.CARDS]},
                json_data_cards,
                indent=4,
            )