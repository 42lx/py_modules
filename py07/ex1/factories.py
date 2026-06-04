from typing import Any

from ex0 import CreatureFactory

from ._creatures import Bloomelle, Morphagon, Shiftling, Sproutling


class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> Any:
        return Sproutling()

    def create_evolved(self) -> Any:
        return Bloomelle()


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> Any:
        return Shiftling()

    def create_evolved(self) -> Any:
        return Morphagon()
