from pydantic import BaseModel
from typing import Self

from .elo_card import EloCard
from .elo import EloTracker

class EloDeck(BaseModel):
    deck : tuple[EloCard, ...]
    id : int

    @property
    def elo(self, )->EloTracker:
        return sum([c.tracker.elo for c in self.deck])/len(self.deck)
    
    @classmethod
    def compute_update_elo(
        self,
        winner:Self,
        loser:Self,
    )->None:

        target_winner, target_loser = EloTracker.compute_elo_diff(
            winner=winner.elo,
            loser=loser.elo,
        )

        for cw in winner.deck:
            cw.update_elo(
                target_elo=target_winner,
                ascending=True
            )

        for cl in loser.deck:
            cl.update_elo(
                target_elo=target_loser,
                ascending=False
            )

