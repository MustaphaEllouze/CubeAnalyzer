from ..constants import CARDS_DATA_JSON_FILE
from ..card_model.card import Card
from .cards_constructor import CardsConstructor

class CardsGetter :
    CARDS = CardsConstructor.contruct_cards(
        json_data=CARDS_DATA_JSON_FILE,
    )

    CARDS_FROM_NAME = {
        c.name:c
        for c in CARDS
    }

    @classmethod
    def get_card_from_name(
        cls,
        card_name:str,
    )->Card:
        return CardsGetter.CARDS_FROM_NAME.get(card_name, None)