import random


class Player:
    def __init__(self, name: str, achievements: set[str]) -> None:
        self.name = name
        self.achievements = achievements

    def unique_among(self, others: list["Player"]) -> set[str]:
        result: set[str] = set(self.achievements)
        for p in others:
            if p is not self:
                result = result.difference(p.achievements)
        return result

    def missing_from(self, all_achs: set[str]) -> set[str]:
        return all_achs.difference(self.achievements)


def gen_player_achievements(all_achs: list[str]) -> set[str]:
    k = random.randint(1, len(all_achs))
    return set(random.sample(all_achs, k=k))


def main() -> None:
    all_achs = [
        "Ach 1", "Ach 2", "Ach 3",
        "Ach 4", "Ach 5", "Ach 6",
        "Ach 7", "Ach 8", "Ach 9",
    ]
    all_achs_set = set(all_achs)
    names = ["Alice", "Bob", "Charlie", "Dylan"]
    players = [Player(n, gen_player_achievements(all_achs)) for n in names]

    print("Achievements system")
    print()
    for p in players:
        print(f"Player {p.name}: {p.achievements}")
    print()
    print(f"All Achievements: {all_achs_set}")
    print()
    common = set.intersection(*(p.achievements for p in players))
    print(f"Common achievements: {common}")
    print()
    for p in players:
        print(f"Only Player {p.name} has: {p.unique_among(players)}")
    print()
    for p in players:
        print(f"Player {p.name} is missing: {p.missing_from(all_achs_set)}")


if __name__ == "__main__":
    main()
