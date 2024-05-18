from ..deck_data.deck_getter import DecksGetter
from ..elo_model.elo_deck import EloDeck
from ..elo_data.elocads_getter import ElocardsGetter

class ElodecksConstructor :

    @classmethod
    def construct_elo_decks(cls, )->tuple[EloDeck]:
        return tuple(
            EloDeck(
                deck = tuple(
                        ElocardsGetter.get_card_from_id(
                            card_id=card.id
                        )
                        for card in deck.cards
                    )
                )
            for deck in DecksGetter.DECKS    
        )