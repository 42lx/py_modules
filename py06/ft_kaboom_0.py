"""ft_kaboom_0: record a light spell via the grimoire module."""
from alchemy.grimoire import light_spell_record


def main() -> None:
    print("=== Kaboom 0 ===")
    print("Using grimoire module directly")
    print(
        "Testing record light spell: "
        f"{light_spell_record('Fantasy', 'Earth, wind and fire')}"
    )


if __name__ == "__main__":
    main()
