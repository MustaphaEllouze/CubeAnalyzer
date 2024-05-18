import json

from ..constants import CARD_ELO_COMPILED_JSON_FILE
from ..elo_model.elo_card import EloCard
from ..elo_data.elocads_getter import ElocardsGetter

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