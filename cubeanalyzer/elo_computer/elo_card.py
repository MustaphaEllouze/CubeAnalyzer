from pydantic import BaseModel
from typing import Self

from ..card_model.card import Card
from .elo import EloTracker

class EloCard(BaseModel):
    card : Card
    tracker : EloTracker

    @classmethod
    def from_card(cls, card:Card):
        return EloCard(
            card=card,
            tracker=EloTracker.initialize_elo(),
        )
    
    def update_elo(
            self,
            target_elo:int,
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