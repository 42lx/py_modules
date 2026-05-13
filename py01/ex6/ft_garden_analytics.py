class Plant:
    class _Stats:
        def __init__(self) -> None:
            self._grow_calls = 0
            self._age_calls = 0
            self._show_calls = 0

        def add_grow(self) -> None:
            self._grow_calls += 1

        def add_age(self) -> None:
            self._age_calls += 1

        def add_show(self) -> None:
            self._show_calls += 1

        def display(self) -> None:
            print(
                f"Stats: {self._grow_calls} grow, "
                f"{self._age_calls} age, "
                f"{self._show_calls} show"
            )

    def __init__(self, name: str, height: float, age: int) -> None:
        self.set_name(name)
        self.set_height(height)
        self.set_age(age)
        self._stats = self._Stats()

    @staticmethod
    def older_than_year(days: int) -> bool:
        return days > 365

    @classmethod
    def anonymous(cls):
        return Plant("Unknown plant", 0.0, 0)

    def get_name(self) -> str:
        return self._name

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_name(self, name: str) -> None:
        self._name = name

    def set_height(self, height: float) -> bool:
        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
            return False
        self._height = height
        return True

    def set_age(self, age: int) -> bool:
        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
            return False
        self._age = age
        return True

    def grow(self, growth_rate: float) -> None:
        if growth_rate > 0:
            self._height += growth_rate
            self._stats.add_grow()

    def age(self, days: int) -> None:
        if days > 0:
            self._age += days
            self._stats.add_age()

    def show(self) -> None:
        self._stats.add_show()
        print(f"{self._name}: {self._height:.1f}cm, {self._age} days old")

    def display_stats(self) -> None:
        self._stats.display()


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self._color = color
        self._has_bloomed = False

    def bloom(self) -> None:
        self._has_bloomed = True

    def show(self) -> None:
        super().show()
        print(f" Color: {self._color}")

        if self._has_bloomed:
            print(f" {self._name} is blooming beautifully!")
        else:
            print(f" {self._name} has not bloomed yet")


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age, color)
        self._seeds = 0

    def bloom(self) -> None:
        super().bloom()
        self._seeds = 42

    def show(self) -> None:
        super().show()
        print(f" Seeds: {self._seeds}")


class Tree(Plant):
    class _TreeStats(Plant._Stats):
        def __init__(self) -> None:
            super().__init__()
            self._shade_calls = 0

        def add_shade(self) -> None:
            self._shade_calls += 1

        def display(self) -> None:
            super().display()
            print(f" {self._shade_calls} shade")

    def __init__(
        self, name: str, height: float, age: int, trunk_diameter: float
    ) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter
        self._stats = self._TreeStats()

    def produce_shade(self) -> None:
        self._stats.add_shade()
        print(
            f"Tree {self._name} now produces a shade "
            f"of {self._height:.1f}cm long and "
            f"{self._trunk_diameter:.1f}cm wide."
        )

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self._trunk_diameter:.1f}cm")


def display_plant_statistics(plant: Plant) -> None:
    print(f"[statistics for {plant.get_name()}]")
    plant.display_stats()


def main():
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.older_than_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.older_than_year(400)}")

    # Flower
    print("\n=== Flower")
    rose = Flower("Rose", 15, 10, "red")
    rose.show()

    display_plant_statistics(rose)

    print("[asking the rose to grow and bloom]")
    rose.grow(8)
    rose.bloom()
    rose.show()

    display_plant_statistics(rose)

    print("\n=== Tree")
    oak = Tree("Oak", 200, 365, 5)
    oak.show()

    display_plant_statistics(oak)

    print("[asking the oak to produce shade]")
    oak.produce_shade()

    display_plant_statistics(oak)

    print("\n=== Seed")
    sunflower = Seed("Sunflower", 80, 45, "yellow")
    sunflower.show()

    print("[make sunflower grow, age and bloom]")
    sunflower.grow(30)
    sunflower.age(20)
    sunflower.bloom()
    sunflower.show()

    display_plant_statistics(sunflower)

    print("\n=== Anonymous")
    unknown = Plant.anonymous()

    unknown.show()
    display_plant_statistics(unknown)


if __name__ == "__main__":
    main()
