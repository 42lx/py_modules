import random


def main() -> None:
    players: list[str] = [
        "Alice", "bob", "Charlie", "dylan",
        "Emma", "Gregory", "john", "kevin", "Liam"
    ]
    print("Initial list of players:", players)
    capitalized: list[str] = [name.capitalize() for name in players]
    print("New list with all names capitalized:", capitalized)
    capitalized_only: list[str] = [
        name for name in players if name[0].isupper()
    ]
    print("New list of capitalized names only:", capitalized_only)
    scores: dict[str, int] = {
        name: random.randint(50, 1000) for name in capitalized
    }
    print("Score dict:", scores)
    avg: float = sum(scores.values()) / len(scores)
    print("Score average is", round(avg, 1))
    high_scores: dict[str, int] = {
        name: score for name, score in
        scores.items() if score > avg
    }
    print("High scores:", high_scores)


if __name__ == "__main__":
    main()
