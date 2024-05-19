import json

from ..constants import CARD_ELO_JSON_FILE
from ..card_data.cards_getter import CardsGetter
from ..elo_model.elo_card import EloCard
from .elocards_constructor import EloCardsConstructor

class ElocardsGetter :
    CARDS = EloCardsConstructor.construct_elo_cards(
        json_data=CARD_ELO_JSON_FILE,
    )

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
    )->EloCard:
        return ElocardsGetter.CARDS_FROM_NAME.get(card_name.capitalize(), None)
    
    @classmethod
    def get_card_from_id(
        cls,
        card_id : int,

    )->EloCard:
        if not card_id in ElocardsGetter.CARDS_FROM_ID : 
            raise ValueError(f'EloCard with ID {card_id} does not exist.')
        return ElocardsGetter.CARDS_FROM_ID.get(card_id, None)
    
    @classmethod
    def get_all_cards(
        cls,
    )->tuple[EloCard]:
        return cls.CARDS
    
    @classmethod
    def add_card_to_database_from_data(
        cls,
        card_id : int,
    )->None:
        
        new_card = EloCard.from_card(
            card=CardsGetter.get_card_from_id(card_id=card_id)
        )
        cls.add_card_to_database(card=new_card)
    
    @classmethod
    def add_card_to_database(cls, card:EloCard)->None:
        if card.id in cls.CARDS_FROM_ID : 
            raise ValueError(f'ID {card.id} is already taken.')
        cls.CARDS += (card, )
        cls.CARDS_FROM_ID[card.id] = card
        cls.CARDS_FROM_NAME[card.name.capitalize()] = card
    
    @classmethod
    def save_database(cls, )->None:
        with open(CARD_ELO_JSON_FILE, 'w') as json_data_cards :
            json.dump(
                {"cards" : [c.to_json() for c in cls.CARDS]},
                json_data_cards,
                indent=4,
            )