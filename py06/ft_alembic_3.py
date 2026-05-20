"""ft_alembic_3: access alchemy/elements.py via 'from ... import ...'."""
from alchemy.elements import create_air


def main() -> None:
    print("=== Alembic 3 ===")
    print(
        "Accessing alchemy/elements.py using "
        "'from ... import ...' structure"
    )
    print(f"Testing create_air: {create_air()}")


if __name__ == "__main__":
    main()
