"""Alchemy package.

Exposes the partial alchemy interface: create_air, potions, and the
transmutation recipe. create_earth is intentionally not exposed at the
package level to demonstrate selective module interfaces.
"""
from .elements import create_air
from .potions import strength_potion
from .potions import healing_potion as heal
from .transmutation.recipes import lead_to_gold

__all__ = ["create_air", "strength_potion", "heal", "lead_to_gold"]
