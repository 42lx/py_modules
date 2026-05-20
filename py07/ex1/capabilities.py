"""Abstract capability mixins."""
from abc import ABC, abstractmethod
from typing import Optional

from ex0 import Creature


class HealCapability(ABC):
    """Healing capability mixin."""

    @abstractmethod
    def heal(self, target: Optional[Creature] = None) -> str:
        ...


class TransformCapability(ABC):
    """Transform capability mixin. Has persistent transformed state."""

    def __init__(self) -> None:
        self.transformed: bool = False

    @abstractmethod
    def transform(self) -> str:
        ...

    @abstractmethod
    def revert(self) -> str:
        ...
