from ..constants import DECK_DATA_JSON_FILE
from ..elo_model.elo_deck import EloDeck
from .elodecks_constructor import ElodecksConstructor

class ElodecksGetter :
    DECKS = ElodecksConstructor.construct_elo_decks(json_data=DECK_DATA_JSON_FILE)

    DECKS_FROM_ID = {
        c.id:c
        for c in DECKS
    }

    @classmethod
    def get_elo_deck_from_id(
        cls,
        deck_id : int,

    )->EloDeck:
        return ElodecksGetter.DECKS_FROM_ID.get(deck_id, None)