from pydantic import BaseModel
from typing import Self

from ..card_model.card import Card
from ..card_model.colors import Color
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

    @property
    def elo(self, )->float:
        return self.tracker.elo

    @property
    def nb_games_done(self, )->float:
        return self.tracker.nb_games_done

    @property
    def color(self, )->tuple[Color, ...]:
        return self.card.color

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
            tracker=EloTracker.initialize_elo().set_elo(elo=elo)
        )
    
    @classmethod
    def from_card_elo_nbgames(cls, card:Card, elo:float, nb_games:int)->Self:
        return EloCard(
            card=card,
            tracker=EloTracker(elo=elo,nb_games_done=nb_games)
        )

    def update_elo(
            self,
            target_elo:float,
            ascending:bool,
    )->None:
        self.tracker.update_towards_this(target=target_elo, ascending=ascending)
    
    def to_json(self, )->dict[str, int|float]:
        return {
            "id" : self.id,
            "elo" : self.elo,
            "nb_games_done" : self.nb_games_done
        }
    
    def set_elo(self, target:float)->None:
        self.tracker.set_elo(elo=target)
    
    def update_games_done(self, nb_games_done:int)->None:
        self.tracker.set_nb_games(nb_games_done)