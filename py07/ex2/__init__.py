"""ex2 package — battle strategy pattern."""
from .exceptions import InvalidStrategyError
from .strategy import (
    AggressiveStrategy,
    BattleStrategy,
    DefensiveStrategy,
    NormalStrategy,
)

__all__ = [
    "BattleStrategy",
    "NormalStrategy",
    "AggressiveStrategy",
    "DefensiveStrategy",
    "InvalidStrategyError",
]
