from pydantic import BaseModel

from ..card_model.card import Card

class Deck(BaseModel):

    cards : tuple[Card, ...]
    id : int