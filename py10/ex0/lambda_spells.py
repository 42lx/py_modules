def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda a: a['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda m: m['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda s: f"* {s} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    return {
        'max_power': max(mages, key=lambda m: m['power'])['power'],
        'min_power': min(mages, key=lambda m: m['power'])['power'],
        'avg_power': round(
            sum(map(lambda m: m['power'], mages)) / len(mages), 2
        ),
    }


def main() -> None:
    artifacts = [
        {'name': 'Fire Staff', 'power': 61, 'type': 'armor'},
        {'name': 'Lightning Rod', 'power': 74, 'type': 'focus'},
        {'name': 'Fire Staff', 'power': 103, 'type': 'relic'},
        {'name': 'Fire Staff', 'power': 97, 'type': 'accessory'},
    ]
    mages = [
        {'name': 'Jordan', 'power': 51, 'element': 'ice'},
        {'name': 'River', 'power': 64, 'element': 'fire'},
        {'name': 'River', 'power': 95, 'element': 'light'},
        {'name': 'Phoenix', 'power': 78, 'element': 'wind'},
        {'name': 'Alex', 'power': 98, 'element': 'lightning'},
    ]
    spells = ['fireball', 'heal', 'shield']

    print("Testing artifact sorter...")
    sorted_artifacts = artifact_sorter(artifacts)
    for a in sorted_artifacts:
        print(f"  {a['name']} ({a['power']} power, {a['type']})")
    first, second = sorted_artifacts[0], sorted_artifacts[1]
    print(
        f"{first['name']} ({first['power']} power) comes before "
        f"{second['name']} ({second['power']} power)"
    )
    print()

    print("Testing power filter (min_power=70)...")
    for m in power_filter(mages, 70):
        print(f"  {m['name']} ({m['power']} power, {m['element']})")
    print()

    print("Testing spell transformer...")
    print(" ".join(spell_transformer(spells)))
    print()

    print("Testing mage stats...")
    print(mage_stats(mages))


if __name__ == "__main__":
    main()
