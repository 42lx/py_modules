"""ft_transmutation_0: lead to gold via direct recipes.py access."""
import alchemy.transmutation.recipes


def main() -> None:
    print("=== Transmutation 0 ===")
    print("Using file alchemy/transmutation/recipes.py directly")
    print(
        "Testing lead to gold: "
        f"{alchemy.transmutation.recipes.lead_to_gold()}"
    )


if __name__ == "__main__":
    main()
