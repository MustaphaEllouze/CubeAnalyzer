from pydantic import BaseModel

from typing import Self
from math import exp

class EloConstants:
    STARTING_ELO = 1000
    OFFSET = 400
    THRESHOLD = 1.0/5.0
    MAX_ELO_CHANGE = 25

class EloTracker(BaseModel):

    # We assume that the knowledge about an elo follows a normal distribution 
    # of mean self.elo and of variance self.variance
    elo : float
    nb_games_done : int

    @classmethod
    def initialize_elo(cls)->Self:
        return EloTracker(
            elo=EloConstants.STARTING_ELO, 
            nb_games_done=1,
        )
    
    @classmethod
    def convert_probability_to_elo_diff(
        cls,
        probability:float,
    )->float:
        assert 0. < probability < 1.

        # The modeling law is computed such as a card that if the difference
        # between ELOs is equal to the OFFSET, than there is a 1-THRESHOLD chance the 
        # stronger card wins, in a vacuum
        # A probability of 100% means that the stronger card has an ELO equal
        # to +inf.
        # If ELOs are equal, than the proability should be equalt to 50% exactly.

        return -EloConstants.OFFSET \
               * (EloConstants.THRESHOLD*(1-EloConstants.THRESHOLD)) \
               / (probability*(1-probability)) \
               * (probability - 0.5) \
               / (EloConstants.THRESHOLD - 0.5) 

    @classmethod
    def convert_elo_diff_to_probability(
        cls,
        elo_diff:float,
    )->float:
        d = elo_diff
        T = EloConstants.THRESHOLD
        C = EloConstants.OFFSET

        if abs(d) < 1e-6 : return 0.5

        first_term = -((4*d**2 * (0.5-T)**2 +4*C**2 * (1-T)**2 * T**2)**0.5 )/4.
        second_term = - 0.5*C*T**2 + 0.5*C*T + d*(0.5*T-0.25)
        third_term = d*(T-0.5)

        return (first_term+second_term)/third_term
    
    def set_elo(self, elo:float):
        self.elo = elo
    
    def set_nb_games(self, nb:int):
        self.nb_games_done = nb
    
    @classmethod
    def update_knowledge_one_game(
        cls,
        tracker1:Self,
        tracker2:Self,
        t1_wins:bool
    )->None:
        
        N = 1
        K = 1 if t1_wins else 0

        elo_diff = tracker1.elo-tracker2.elo
        proba = EloTracker.convert_elo_diff_to_probability(elo_diff)
        mean_done_games = int((tracker1.nb_games_done+tracker2.nb_games_done)*0.5)

        new_elo_difference = EloTracker.convert_probability_to_elo_diff(
            probability=(proba*mean_done_games+K)/(mean_done_games+N)
        )
        
        # As the product of the ELOs is to remain constant, we have :
        # e1.e2 = e1'.e2'
        # new_elo_difference = e1-e2
        # which yields after some computation to this formulas
        e1p = 0.5* (
            (new_elo_difference**2 + 4*tracker1.elo*tracker2.elo)**0.5
            +new_elo_difference
        )
        e2p = 0.5* (
            (new_elo_difference**2 + 4*tracker1.elo*tracker2.elo)**0.5
            -new_elo_difference
        )

        # Multiplication factor for elo_difference
        coeff_t1wins = 1 if elo_diff < 0 else (exp(-elo_diff/EloConstants.OFFSET)-exp(-1))/(1-exp(-1))
        coeff_t1wins = max(coeff_t1wins, 0)
        coeff_t2wins = 1 if elo_diff > 0 else (exp(elo_diff/EloConstants.OFFSET)-exp(-1))/(1-exp(-1))
        coeff_t2wins = max(coeff_t2wins, 0)

        # nb games 
        tracker1.set_nb_games(tracker1.nb_games_done+N)
        tracker2.set_nb_games(tracker2.nb_games_done+N)

        ## Update the data
        if t1_wins : 
            coeff = coeff_t1wins
        else :
            coeff = coeff_t2wins

        new_e1 = max(tracker1.elo + (e1p-tracker1.elo)*coeff, tracker1.elo - EloConstants.MAX_ELO_CHANGE)
        new_e1 = min(new_e1, tracker1.elo + EloConstants.MAX_ELO_CHANGE)
        new_e2 = max(tracker2.elo + (e2p-tracker2.elo)*coeff, tracker2.elo - EloConstants.MAX_ELO_CHANGE)
        new_e2 = min(new_e2, tracker2.elo + EloConstants.MAX_ELO_CHANGE)

        tracker1.set_elo(new_e1)
        tracker2.set_elo(new_e2)
    
    @classmethod
    def update_knowledge(
        cls,
        tracker1:Self,
        tracker2:Self,
        t1wins:int,
        t2wins:int,
    )->None:
        for _ in range(t1wins-t2wins) : cls.update_knowledge_one_game(tracker1,tracker2,True)
        for _ in range(t2wins-t1wins) : cls.update_knowledge_one_game(tracker1,tracker2,False)
    
    def update_towards_this(
            self,
            target:float,
            ascending:bool,
            coefficient:float=1.,
    )->None:
        if (target>=self.elo and ascending) or (target<=self.elo and not ascending):
            self.set_elo(self.elo+(target-self.elo)*coefficient)