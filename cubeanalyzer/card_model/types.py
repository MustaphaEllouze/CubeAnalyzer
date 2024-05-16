from dataclasses import dataclass
from enum import Enum

@dataclass
class TypeData:
    name : str
    symbol : str

class CardType(Enum):
    ARTIFACT     = TypeData(name='artifact',    symbol='a')
    CREATURE     = TypeData(name='creature',    symbol='c')
    LAND         = TypeData(name='land',        symbol='l')
    INSTANT      = TypeData(name='instant',     symbol='i')
    SORCERY      = TypeData(name='sorcery',     symbol='s')
    ENCHANTEMENT = TypeData(name='enchantment', symbol='e')
    BATTLE       = TypeData(name='battle',      symbol='b')
    KINDRED      = TypeData(name='kindred',     symbol='k')

SYMBOL_TO_TYPE = {c.value.symbol:c for c in CardType}
NAME_TO_TYPE   = {c.value.name:c   for c in CardType}

def get_type(card_type_name:str)->CardType:
    """Return a card type from its name of its symbol."""

    try_name = NAME_TO_TYPE.get(card_type_name, None)
    try_symbol = SYMBOL_TO_TYPE.get(card_type_name, None)

    if try_name : return try_name
    if try_symbol : return try_symbol

    raise ValueError(
        f'Invalid card type name, got {card_type_name}, expected a symbol' \
        f'({list(SYMBOL_TO_TYPE.keys())}) or a name '\
        f'({list(NAME_TO_TYPE.keys())}).'
    )