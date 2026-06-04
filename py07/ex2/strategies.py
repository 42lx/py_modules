from abc import ABC, abstractmethod
from typing import Any

from ex1 import HealCapability, TransformCapability

from .exceptions import InvalidStrategyError


class BattleStrategy(ABC):
    @abstractmethod
    def is_valid(self, creature: Any) -> bool:
        ...

    @abstractmethod
    def act(self, creature: Any) -> None:
        ...


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Any) -> bool:
        return True

    def act(self, creature: Any) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.name}' for this normal strategy"
            )
        print(creature.attack())


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Any) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Any) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.name}' "
                f"for this aggressive strategy"
            )
        print(creature.transform())
        print(creature.attack())
        print(creature.revert())


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Any) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Any) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.name}' "
                f"for this defensive strategy"
            )
        print(creature.attack())
        print(creature.heal())
