from pydantic import BaseModel

from ..elo_model.elo_deck import EloDeck

class Game(BaseModel):
    deck1 : EloDeck
    deck2 : EloDeck

    def deck1_wins(
            self,
    )->None:
        EloDeck.compute_update_elo(
            winner=self.deck1,
            loser=self.deck2
        )
    
    def deck2_wins(
            self
    )->None:
        EloDeck.compute_update_elo(
            winner=self.deck2,
            loser=self.deck1,
        )

    @classmethod
    def register_game(
        cls,
        deck1 : EloDeck,
        deck2 : EloDeck,
        deck1_wins : int,
        deck2_wins : int
    )->None :
        matchup = Game(
            deck1=deck1,
            deck2=deck2
        )

        # Only call wins function if the difference is positive (therefore, 
        # it the elo difference is not dependent on the order of the operations)
        for _ in range(deck1_wins-deck2_wins) : matchup.deck1_wins()
        for _ in range(deck2_wins-deck1_wins) : matchup.deck2_wins()