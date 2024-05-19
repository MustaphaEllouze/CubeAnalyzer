from pydantic import BaseModel

from typing import Self

STARTING_ELO = 1000
MAX_OFFSET = 400
SCALING_COEF = 0.1

class EloTracker(BaseModel):
    elo : float

    @classmethod
    def initialize_elo(cls)->Self:
        return EloTracker(elo=STARTING_ELO)
    
    @classmethod
    def compute_elo_diff(
        cls,
        winner:float,
        loser:float,
    )->tuple[float, float]:

        return max(loser + MAX_OFFSET, winner), min(winner - MAX_OFFSET, loser)

    def update_elo(
            self,
            target_elo:float,
            ascending:bool,    
        )->None:
        if (ascending and target_elo > self.elo) \
            or (not ascending and target_elo < self.elo) :
            self.elo += (target_elo-self.elo)*SCALING_COEF
    
    def set_elo(
            self,
            target:float,
    )->None:
        self.elo = target
    
    @classmethod
    def compute_and_update(
        cls, 
        winner:Self, 
        loser:Self,
    )->None:
        new_w_elo, new_l_elo = EloTracker.compute_elo_diff(
            winner=winner.elo,
            loser=loser.elo,
        )
        winner.update_elo(new_w_elo, ascending=True)
        loser.update_elo(new_l_elo, ascending=False)
        