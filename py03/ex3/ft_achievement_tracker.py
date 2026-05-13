import random


def gen_player_achievements(all_achs: list[str]) -> set[str]:
    return set(random.sample(all_achs, k=random.randint(1, len(all_achs))))


def main() -> None:
    all_achs = [
            "Achievment 1",
            "Achievment 2",
            "Achievment 3",
            "Achievment 4",
            "Achievment 5",
            "Achievment 6",
            "Achievment 7",
            "Achievment 8",
            "Achievment 9",
            ]
    all_achs_set = set(all_achs)
    players = [
            gen_player_achievements(all_achs),
            gen_player_achievements(all_achs),
            gen_player_achievements(all_achs),
            gen_player_achievements(all_achs)
            ]
    print(players)
    shared = set.intersection(*players)
    unique_achs_0 = players[0].difference()
    print()
    print(shared)
    print(unique_achs_0)


if __name__ == "__main__":
    main()
