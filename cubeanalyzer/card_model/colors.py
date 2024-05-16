from dataclasses import dataclass
from enum import Enum

@dataclass
class ColorData :
    name : str
    symbol : str

class Color(Enum) :
    WHITE = ColorData(name='white', symbol='W')
    BLUE  = ColorData(name='blue' , symbol='U')
    BLACK = ColorData(name='black', symbol='B')
    RED   = ColorData(name='red'  , symbol='R')
    GREEN = ColorData(name='green', symbol='G')

SYMBOL_TO_COLOR = {c.value.symbol:c for c in Color}
NAME_TO_COLOR   = {c.value.name:c   for c in Color}

def get_color(color_name:str)->Color:
    """Return a color from its name of its symbol."""

    try_name = NAME_TO_COLOR.get(color_name, None)
    try_symbol = SYMBOL_TO_COLOR.get(color_name, None)

    if try_name : return try_name
    if try_symbol : return try_symbol

    raise ValueError(
        f'Invalid color name, got {color_name}, expected a symbol' \
        f'({list(SYMBOL_TO_COLOR.keys())}) or a name '\
        f'({list(NAME_TO_COLOR.keys())}).'
    )