"""Grimoire subpackage.

Exposes only the light spellbook entry point. The dark counterpart is
left out so importing the package does not trigger the circular import
demonstrated in ft_kaboom_1.py.
"""
from .light_spellbook import light_spell_record

__all__ = ["light_spell_record"]
