import math


def get_player_pos() -> tuple[float, float, float] | None:
    while True:
        try:
            user_input = input("Input coords as x, y, z:")
            parts = user_input.split(",")
        except (KeyboardInterrupt, EOFError):
            print("\nInterrupted by user")
            return None
        try:
            x_str, y_str, z_str = parts
            x = float(x_str.strip())
            y = float(y_str.strip())
            z = float(z_str.strip())
            return (x, y, z)
        except ValueError:
            print("Invalid format or not exactly 3 numbers. Try again.")


def calc_dist(
        p1: tuple[float, float, float],
        p2: tuple[float, float, float]
        ) -> float:
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return math.sqrt(
            (x2 - x1) ** 2
            + (y2 - y1) ** 2
            + (z2 - z1) ** 2
            )


def print_point(p: tuple[float, float, float]) -> None:
    x, y, z = p
    print("Tuple:", p)
    print(f"It includes x={x}, y={y}, z={z}")


def main() -> None:
    print("First set of coords:")
    p1 = get_player_pos()
    if p1 is None:
        return
    print_point(p1)
    print("Distance to center:", calc_dist(p1, (0.0, 0.0, 0.0)))
    print()
    print("Second set of coords:")
    p2 = get_player_pos()
    if p2 is None:
        return
    print("Distance between p1 and p2:", calc_dist(p1, p2))


if __name__ == "__main__":
    main()
