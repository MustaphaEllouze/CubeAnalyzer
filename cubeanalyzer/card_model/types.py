from dataclasses import dataclass
from enum import Enum

@dataclass
class TypeData:
    name : str
    symbol : str

class CardType(Enum):
    ARTIFACT     = TypeData(name='artifact',    symbol='A')
    CREATURE     = TypeData(name='creature',    symbol='C')
    LAND         = TypeData(name='land',        symbol='L')
    INSTANT      = TypeData(name='instant',     symbol='I')
    SORCERY      = TypeData(name='sorcery',     symbol='S')
    ENCHANTEMENT = TypeData(name='enchantment', symbol='E')
    BATTLE       = TypeData(name='battle',      symbol='B')
    KINDRED      = TypeData(name='kindred',     symbol='K')
    PLANESWALKER = TypeData(name='planeswalker',symbol='P')
    LEGENDARY    = TypeData(name='legendary'   ,symbol='LGD')
    SNOW         = TypeData(name='snow'        ,symbol='SNW')
    HUMAN        = TypeData(name='human'       ,symbol='HUMAN')
    KNIGHT       = TypeData(name='knight'      ,symbol='KNIGHT')

SYMBOL_TO_TYPE = {c.value.symbol:c for c in CardType}
NAME_TO_TYPE   = {c.value.name:c   for c in CardType}

def get_type(card_type_name:str)->CardType:
    """Return a card type from its name of its symbol."""

    try_name = NAME_TO_TYPE.get(card_type_name.lower(), None)
    try_symbol = SYMBOL_TO_TYPE.get(card_type_name.capitalize(), None)

    if try_name : return try_name
    if try_symbol : return try_symbol

    raise ValueError(
        f'Invalid card type name, got {card_type_name}, expected a symbol' \
        f'({list(SYMBOL_TO_TYPE.keys())}) or a name '\
        f'({list(NAME_TO_TYPE.keys())}).'
    )

def get_type_list(card_type_names:list[str])->list[CardType]:
    return [get_type(t) for t in card_type_names]