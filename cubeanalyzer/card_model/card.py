from pydantic import BaseModel
from typing import Self

from .colors import Color, get_color
from .types import CardType, get_type

class Card(BaseModel):
    name : str
    color : Color
    mana_value : int
    card_types : tuple[CardType]

    def __str__(self, )->str:
        return f'Card('\
               f'name="{self.name}", '\
               f'color={self.color}, '\
               f'card_types={self.card_types}, '\
               f'mana_value={self.mana_value}'\
               f')'
    
    @classmethod
    def from_data(
        cls,
        name:str,
        color:str,
        mana_value:int,
        card_types : tuple[str]
    )->Self:
        return Card(
            name=name,
            color=get_color(color),
            mana_value=mana_value,
            card_types=tuple(get_type(t) for t in card_types)
        )