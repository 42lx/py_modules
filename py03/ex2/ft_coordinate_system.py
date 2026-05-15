import math


def get_player_pos() -> tuple[float, float, float] | None:
    while True:
        try:
            strs = input("Input coords as x, y, z:").split(",")
        except KeyboardInterrupt:
            print("Interrupted by user")
            return None
        try:
            res = [float(str.strip()) for str in strs]
            return (res[0], res[1], res[2])
        except Exception:
            print("Invalid. Try again")


def calc_dist(
        p1: tuple[float, float, float],
        p2: tuple[float, float, float]
        ) -> float:
    return math.sqrt(
            (p2[0] - p1[0]) ** 2
            + (p2[1] - p1[1]) ** 2
            + (p2[2] - p1[2]) ** 2
            )


def print_point(p: tuple[float, float, float]) -> None:
    print("Tuple:", p)
    print(f"It includes x={p[0]}, y={p[1]}, z={p[2]}")


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
