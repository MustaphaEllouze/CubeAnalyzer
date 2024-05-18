from ..constants import CARD_ELO_JSON_FILE
from ..elo_model.elo_card import EloCard
from .elocards_constructor import EloCardsConstructor

class ElocardsGetter :
    CARDS = EloCardsConstructor.construct_elo_cards(
        json_data=CARD_ELO_JSON_FILE,
    )

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
    )->EloCard:
        return ElocardsGetter.CARDS_FROM_NAME.get(card_name, None)
    
    @classmethod
    def get_card_from_id(
        cls,
        card_id : int,

    )->EloCard:
        if not card_id in ElocardsGetter.CARDS_FROM_ID : 
            raise ValueError(f'EloCard with ID {card_id} does not exist.')
        return ElocardsGetter.CARDS_FROM_ID.get(card_id, None)