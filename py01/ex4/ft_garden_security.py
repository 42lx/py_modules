class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.set_name(name)
        self.set_height(height)
        self.set_age(age)

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
        self._height += growth_rate

    def age(self) -> None:
        self._age += 1

    def show(self) -> None:
        print(f"{self._name}: {self._height:.1f}cm, {self._age} days old")


def main() -> None:
    print("=== Garden Security System ===")

    plant = Plant("Rose", 15, 10)
    print("Plant created: ", end="")
    plant.show()
    print()

    if plant.set_height(25):
        print(f"Height updated: {plant.get_height()}cm")
    else:
        print("Height update rejected")

    if plant.set_age(30):
        print(f"Age updated: {plant.get_age()} days")
    else:
        print("Age update rejected")

    print()

    if plant.set_height(-10):
        print(f"Height updated: {plant.get_height()}cm")
    else:
        print("Height update rejected")

    if plant.set_age(-10):
        print(f"Age updated: {plant.get_age()} days")
    else:
        print("Age update rejected")

    print()
    print("Current state: ", end="")
    plant.show()


if __name__ == "__main__":
    main()
