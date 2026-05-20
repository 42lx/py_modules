"""ex0 package — abstract factory pattern.

Exposes only the Creature ABC and factories. Concrete Creature classes
are not exported, per the assignment constraint.
"""
from .creature import Creature
from .factories import AquaFactory, CreatureFactory, FlameFactory

__all__ = ["Creature", "CreatureFactory", "FlameFactory", "AquaFactory"]
