import json
from typing import Any

from ..card_model.card import Card

class CardsConstructor :

    @classmethod
    def contruct_cards(cls, json_data:str)->tuple[Card]:

        # Read data the json card data file, then create corresponding cards
        with open(json_data) as json_file :
            data : list[dict[str, Any]] = json.load(json_file)['cards']

        # Iterable of cards
        cards = tuple(
            Card.from_data(
                name = card.get('name', None),
                color = card.get('color', None),
                mana_value = card.get('mana_value', None),
                card_types = card.get('card_types', None)
            )
            for card in data   
        )

        return cards