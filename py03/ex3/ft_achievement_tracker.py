import random


def gen_player_achievements(all_achs: list[str]) -> set[str]:
    return set(random.sample(all_achs, k=random.randint(1, len(all_achs))))


def unique_to(target: set[str], all_sets: list[set[str]]) -> set[str]:
    result = target
    for s in all_sets:
        if s is not target:
            result = result.difference(s)
    return result


def main() -> None:
    all_achs = [
        "Ach 1",
        "Ach 2",
        "Ach 3",
        "Ach 4",
        "Ach 5",
        "Ach 6",
        "Ach 7",
        "Ach 8",
        "Ach 9",
    ]
    all_achs_set = set(all_achs)
    names = ["Alice", "Bob", "Charlie", "Dylan"]
    players = [
        gen_player_achievements(all_achs),
        gen_player_achievements(all_achs),
        gen_player_achievements(all_achs),
        gen_player_achievements(all_achs),
    ]

    print("Achievements system")
    print()
    i = 0
    for player in players:
        print(f"Player {names[i]}:", player)
        i += 1
    print()
    print("All Achievements:", all_achs_set)
    print()
    print("Common achievments:", set.intersection(*players))
    print()
    i = 0
    for player in players:
        print(f"Only Player {names[i]} has:", unique_to(player, players))
        i += 1
    print()
    i = 0
    for player in players:
        print(
            f"Player {names[i]} is missing:",
            all_achs_set.difference(player)
        )
        i += 1


if __name__ == "__main__":
    main()
