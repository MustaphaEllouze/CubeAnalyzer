from pydantic import BaseModel
from typing import Self

from .elo_card import EloCard
from .elo import EloTracker

class EloDeck(BaseModel):
    deck : tuple[EloCard, ...]
    id : int

    @property
    def elo(self, )->EloTracker:
        return sum([c.elo for c in self.deck])/len(self.deck)
    
    @classmethod
    def compute_update_elo(
        cls,
        winner:Self,
        loser:Self,
    )->None:

        # create new trackers that mimic those of cards
        nb_games_winner = int(sum([c.nb_games_done for c in winner.deck])/len(winner.deck))
        nb_games_loser = int(sum([c.nb_games_done for c in loser.deck])/len(loser.deck))

        # Pseudo trackers
        t1 = EloTracker(elo=winner.elo, nb_games_done=nb_games_winner)
        t2 = EloTracker(elo=loser.elo, nb_games_done=nb_games_loser)

        EloTracker.update_knowledge_one_game(t1, t2, True)

        # get new elos
        winner_mean_elo = t1.elo
        loser_mean_elo = t2.elo


        for cw in winner.deck:
            cw.update_elo(
                target_elo=cw.elo+(winner_mean_elo-winner.elo),
                ascending=True
            )
            cw.update_games_done(cw.nb_games_done+1)

        for cl in loser.deck:
            cl.update_elo(
                target_elo=cl.elo+(loser_mean_elo-loser.elo),
                ascending=False
            )
            cl.update_games_done(cl.nb_games_done+1)

