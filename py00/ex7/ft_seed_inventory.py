def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    to_print: str = seed_type.capitalize() + " seeds: "
    if unit == "packets":
        to_print = to_print + f"{quantity} packets available"
    elif unit == "grams":
        to_print = to_print + f"{quantity} grams total"
    elif unit == "area":
        to_print = to_print + f"covers {quantity} square meters"
    else:
        print("Unknown unit type")
        return
    print(to_print)
