import json

from ..constants import CARD_ELO_COMPILED_JSON_FILE
from ..elo_data.elocards_getter import ElocardsGetter
from ..elo_model.elo import STARTING_ELO, MAX_OFFSET

class EloModifier:
    
    @classmethod
    def __convert_dict_to_elo_file(
        cls, 
        json_dict:dict,
    )->None:
        with open(CARD_ELO_COMPILED_JSON_FILE, 'w') as writable_file:
            json.dump(
                json_dict,
                writable_file,
                indent=4,
            )
    
    @classmethod
    def update_json_elo_cards(
        cls,
    )->None:
        EloModifier.__convert_dict_to_elo_file(
            json_dict={
                "cards" : [
                    {
                        "id" : c.id,
                        "elo" : c.elo
                    }
                    for c in ElocardsGetter.get_all_cards()
                ]
            }
        )
    
    @classmethod
    def set_elo_distribution(
        cls,
        target_mean:float=STARTING_ELO,
        target_standard_deviation:float=0.5*MAX_OFFSET,
    )->None:
        
        all_elo_cards = ElocardsGetter.get_all_cards()

        # Curret mean/standard deviation
        current_mean = sum([c.elo for c in all_elo_cards])/len(all_elo_cards)
        current_standard_deviation = (sum(
            [
                (c.elo-current_mean)**2
                for c in all_elo_cards
            ]
        )/len(all_elo_cards))**(0.5)

        if abs(current_standard_deviation)<1e-6 : 
            current_standard_deviation = target_standard_deviation

        # Scaling
        for c in all_elo_cards:
            c.set_elo(
                target=target_mean+(c.elo-current_mean)
                        *target_standard_deviation
                        /current_standard_deviation
            )
