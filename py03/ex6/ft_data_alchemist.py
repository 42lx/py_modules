import random


def main() -> None:
    print("=== Game Data Alchemist ===\n")
    players = [
        'Alice', 'bob', 'Charlie', 'dylan',
        'Emma', 'Gregory', 'john', 'kevin', 'Liam'
    ]
    print("Initial list of players:", players)
    capitalized = [name.capitalize() for name in players]
    print("New list with all names capitalized:", capitalized)
    capitalized_only = [name for name in players if name[0].isupper()]
    print("New list of capitalized names only:", capitalized_only)
    scores = {name: random.randint(50, 1000) for name in capitalized}
    print("Score dict:", scores)
    avg = sum(scores.values()) / len(scores)
    print("Score average is", round(avg, 1))
    high_scores = {
        name: score for name, score in
        scores.items() if score > avg
    }
    print("High scores:", high_scores)


if __name__ == "__main__":
    main()
