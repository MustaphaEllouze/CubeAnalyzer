from pydantic import BaseModel
from typing import Self

from ..card_model.card import Card
from .elo import EloTracker

class EloCard(BaseModel):
    card : Card
    tracker : EloTracker

    @property
    def name(self, )->str:
        return self.card.name
    
    @property
    def id(self, )->int:
        return self.card.id

    @classmethod
    def from_card(cls, card:Card)->Self:
        return EloCard(
            card=card,
            tracker=EloTracker.initialize_elo(),
        )
    
    @classmethod
    def from_card_and_elo(cls, card:Card, elo:float)->Self:
        return EloCard(
            card=card,
            tracker=EloTracker(elo = elo)
        )

    def update_elo(
            self,
            target_elo:float,
            ascending:bool,
    )->None:
        self.tracker.update_elo(target_elo=target_elo, ascending=ascending)
    
    @classmethod
    def compute_update_elo(
        cls,
        winner : Self,
        loser : Self,
    )->None:
        EloTracker.compute_and_update(
            winner=winner.tracker,
            loser=loser.tracker,
        )