from pydantic import BaseModel
from typing import Self

from .colors import Color, get_color_list
from .types import CardType, get_type

class Card(BaseModel):
    name : str
    color : tuple[Color, ...]
    mana_value : int
    card_types : tuple[CardType, ...]
    id : int

    def __str__(self, )->str:
        return f'Card('\
               f'name="{self.name}", '\
               f'color={self.color}, '\
               f'card_types={self.card_types}, '\
               f'mana_value={self.mana_value}, '\
               f'id={self.id}'\
               f')'
    
    @classmethod
    def from_data(
        cls,
        name:str,
        color:tuple[str],
        mana_value:int,
        card_types : tuple[str],
        id : int
    )->Self:
        return Card(
            name=name,
            color=get_color_list(color),
            mana_value=mana_value,
            card_types=tuple(get_type(t) for t in card_types),
            id=id,
        )

    def to_json(self, )->dict[str,str|int]:
        return {
            "name" : self.name,
            "color" : [c.value.name for c in self.color],
            "mana_value" : self.mana_value,
            "card_types" : [t.value.name for t in self.card_types],
            "id" : self.id,
        }