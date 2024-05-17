import json
from typing import Any

from ..deck_model.deck import Deck
from ..card_data.cards_getter import CardsGetter

class DeckConstructor :

    @classmethod
    def contruct_decks(cls, json_data:str)->tuple[Deck]:

        # Read data the json deck data file, then create corresponding decks
        with open(json_data) as json_file :
            data : list[dict[str, Any]] = json.load(json_file)['decks']

        # Iterable of decks
        decks = tuple(
            Deck(
                cards=[
                    CardsGetter.get_card_from_id(card_id=id)
                    for id in deck.get('cards_id', None)
                ],
                id = deck.get('id', None)
            )
            for deck in data   
        )

        return decks