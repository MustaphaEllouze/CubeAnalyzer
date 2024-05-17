from ..constants import DECK_DATA_JSON_FILE
from ..deck_model.deck import Deck
from .deck_constructor import DeckConstructor

class DecksGetter :
    DECKS = DeckConstructor.contruct_decks(
        json_data=DECK_DATA_JSON_FILE,
    )

    # Check that there is unique IDs
    __check_id_list = []
    for c in DECKS :
        if c.id in __check_id_list : 
            raise ValueError(f'ID {c.id} is used twice.')
        __check_id_list.append(c.id)

    DECKS_FROM_ID = {
        c.id:c
        for c in DECKS
    }

    @classmethod
    def get_deck_from_id(
        cls,
        deck_id : int,

    )->Deck:
        return DecksGetter.DECKS_FROM_ID.get(deck_id, None)