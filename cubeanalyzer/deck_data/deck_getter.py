import json

from ..constants import DECK_DATA_JSON_FILE
from ..deck_model.deck import Deck
from .deck_constructor import DeckConstructor
from ..card_model.card import Card

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

    @classmethod
    def add_deck_to_database_from_data(
        cls,
        cards:tuple[Card],
    )->None:
        
        max_id = max([d.id for d in cls.DECKS]) if cls.DECKS else 0
        new_deck = Deck(
            cards=cards,
            id=max_id+1,
        )
        cls.add_deck_to_database(deck=new_deck)
    
    @classmethod
    def add_deck_to_database(cls, deck:Deck)->None:
        if deck.id in cls.DECKS_FROM_ID : 
            raise ValueError(f'Deck ID {deck.id} is already taken.')
        cls.DECKS += (deck, )
        cls.DECKS_FROM_ID[deck.id] = deck
    
    @classmethod
    def save_database(cls, )->None:
        with open(DECK_DATA_JSON_FILE, 'w') as json_data_decks :
            json.dump(
                {"decks" : [d.to_json() for d in cls.DECKS]},
                json_data_decks,
                indent=4,
            )