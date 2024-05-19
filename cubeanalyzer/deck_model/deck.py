from pydantic import BaseModel

from ..card_model.card import Card

class Deck(BaseModel):

    cards : tuple[Card, ...]
    id : int

    def to_json(self, )->dict[str, list[int]|int]:
        return {
            "cards_id" : [c.id for c in self.cards],
            "id" : self.id,
        }