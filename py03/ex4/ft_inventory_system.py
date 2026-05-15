import sys


def parse_arg(arg: str) -> tuple[str, int] | None:
    parts = arg.split(":")
    if len(parts) != 2 or len(parts[0]) == 0:
        return None
    try:
        qty = int(parts[1])
    except ValueError:
        return None
    return (parts[0], qty)


def build_inventory(args: list[str]) -> dict[str, int]:
    inv: dict[str, int] = {}
    for arg in args:
        parsed = parse_arg(arg)
        if parsed is None:
            print(f"Error: invalid parameter {arg}")
            continue
        name, qty = parsed
        if name in inv.keys():
            print(f"Redundant item {name} - discarding")
            continue
        inv.update({name: qty})
    return inv


def report_percentages(inv: dict[str, int], total: int) -> None:
    for name in inv.keys():
        pct = inv[name] / total * 100
        print(f"Item {name} represents {pct:.1f}%")


def report_extremes(inv: dict[str, int]) -> None:
    items = list(inv.keys())
    most = items[0]
    least = items[0]
    for name in items:
        if inv[name] > inv[most]:
            most = name
        if inv[name] < inv[least]:
            least = name
    print(f"Most abundant: {most} with quantity {inv[most]}")
    print(f"Least abundant: {least} with quantity {inv[least]}")


def main() -> None:
    print("Inventory System")
    inv = build_inventory(sys.argv[1:])

    print(f"Got inventory: {inv}")
    print(f"Item list: {list(inv.keys())}")
    if len(inv) == 0:
        print("No items in inventory.")
    else:
        total = sum(inv.values())
        print(f"Total quantity of the {len(inv)} items: {total}")
        report_percentages(inv, total)
        report_extremes(inv)
    inv.update({"magic_item": 1})
    print(f"Updated inventory: {inv}")


if __name__ == "__main__":
    main()
