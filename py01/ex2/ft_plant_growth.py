class Plant:
    def __init__(self, name: str, height: float, days: int) -> None:
        self.name = name
        self.height = height
        self.days = days

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.days} days old")

    def grow(self, growth: float) -> None:
        self.height += growth

    def age(self) -> None:
        self.days += 1


def main() -> None:
    print("=== Garden Plant Registry ===")

    plant = Plant("Lily", 8, 5)
    plant.show()
    initial_height = plant.height

    for day in range(1, 12):
        print(f"=== Day {day} ===")
        plant.grow(1.5)
        plant.age()
        plant.show()

    growth = plant.height - initial_height
    print(f"Growth this week: {growth:.1f}cm")


if __name__ == "__main__":
    main()
