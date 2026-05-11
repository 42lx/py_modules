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

    plants = [
            Plant("Basil", 8, 5),
            Plant("Rosemary", 4, 4),
            Plant("Thyme", 20, 15),
            Plant("Mint", 34, 33),
            Plant("Lavender", 42, 42),
    ]

    print("=== Plant Factory Output ===")
    for plant in plants:
        print("Created: ", end="")
        plant.show()



if __name__ == "__main__":
    main()
