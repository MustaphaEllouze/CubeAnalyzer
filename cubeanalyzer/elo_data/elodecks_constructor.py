from ..deck_data.deck_constructor import DeckConstructor
from ..elo_model.elo_deck import EloDeck
from ..elo_data.elocards_getter import ElocardsGetter

class ElodecksConstructor :

    @classmethod
    def construct_elo_decks(cls, json_data:str)->tuple[EloDeck]:
        return tuple(
            EloDeck(
                deck = tuple(
                        ElocardsGetter.get_card_from_id(
                            card_id=card.id
                        )
                        for card in deck.cards
                    ),
                id=deck.id,
                )
            for deck in DeckConstructor.contruct_decks(json_data=json_data)    
        )