from typing import Any
import json

from ..elo_model.elo_card import EloCard
from..card_data.cards_getter import CardsGetter

class EloCardsConstructor :

    @classmethod
    def construct_elo_cards(
        cls,
        json_data:str
    )->tuple[EloCard]:
        # Read data from the json elo cards data file, then create corresponding
        # cards
        with open(json_data) as json_file:
            data : list[dict[str, Any]] = json.load(json_file)['cards']

        # Iterable of elo cards
        elocards = tuple(
            EloCard.from_card_elo_nbgames(
                card=CardsGetter.get_card_from_id(card_id=c.get('id', None)),
                elo=c.get('elo', None),
                nb_games=c.get('nb_games_done',None),
            )
            for c in data
        )

        return elocards
