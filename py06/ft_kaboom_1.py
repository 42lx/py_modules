"""ft_kaboom_1: dark spellbook import collapses on a circular dependency."""

print("=== Kaboom 1 ===")
print("Access to alchemy/grimoire/dark_spellbook.py directly")
print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")

from alchemy.grimoire.dark_spellbook import dark_spell_record  # noqa: E402

print(f"Testing record dark spell: {dark_spell_record('Necromancy', 'bats')}")
