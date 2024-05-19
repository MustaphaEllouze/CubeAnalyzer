from ..constants import DECKS_METAFILE
from ..card_data.cards_getter import CardsGetter
from ..deck_data.deck_getter import DecksGetter

class DecksParser:

    DECK_SEPARATOR = '/deck/'
    CARDS_SEPARATOR = '\n'

    @classmethod
    def parse_metafile(cls, )->None:
        with open(DECKS_METAFILE, 'r') as decks_metafile:
            data = decks_metafile.read()
        
        # First chunk is skipped because it doesn't start by the separator
        # by construction
        decks = data.split(cls.DECK_SEPARATOR)[1:]
        
        for deck in decks:
            deck_content = deck.strip().split('\n')
            deck_content_name = [d for d in deck_content if d]
            deck_content_card = [
                CardsGetter.get_card_from_name(card_name=name)
                for name in deck_content_name
            ]
            for name,possible_id in zip(deck_content_name, deck_content_card):
                if not possible_id:
                    raise ValueError(f'Unrecoginzed card name: {name}')
            DecksGetter.add_deck_to_database_from_data(
                cards = deck_content_card
            )
        
        DecksGetter.save_database()

        # Delete the metafile
        with open(DECKS_METAFILE, 'w') : pass



