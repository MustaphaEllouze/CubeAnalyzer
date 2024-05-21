from pydantic import BaseModel

from ..elo_model.elo_deck import EloDeck

class Game(BaseModel):
    deck1 : EloDeck
    deck2 : EloDeck
    deck1_wins : int
    deck2_wins : int

    def compute_elo_deck1_wins(
            self,
    )->None:
        EloDeck.compute_update_elo(
            winner=self.deck1,
            loser=self.deck2
        )
    
    def compute_elo_deck2_wins(
            self
    )->None:
        EloDeck.compute_update_elo(
            winner=self.deck2,
            loser=self.deck1,
        )
    
    def register_results(self, )->None:
        # Only call wins function if the difference is positive (therefore, 
        # it the elo difference is not dependent on the order of the operations)
        for _ in range(self.deck1_wins-self.deck2_wins) : self.compute_elo_deck1_wins()
        for _ in range(self.deck2_wins-self.deck1_wins) : self.compute_elo_deck2_wins()

    @classmethod
    def register_game(
        cls,
        deck1 : EloDeck,
        deck2 : EloDeck,
        deck1_wins : int,
        deck2_wins : int
    )->None :
        Game(
            deck1=deck1,
            deck2=deck2,
            deck1_wins=deck1_wins,
            deck2_wins=deck2_wins,
        ).register_results()
    
    def to_json(self, )->dict[str, int]:
        return {
            "deck1_id" : self.deck1.id,
            "deck2_id" : self.deck2.id,
            "deck1_wins" : self.deck1_wins,
            "deck2_wins" : self.deck2_wins
        }