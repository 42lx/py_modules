class GardenError(Exception):
    def __init__(self, msg: str = "Some garden msg") -> None:
        super().__init__(msg)


class PlantError(GardenError):
    def __init__(self, msg: str = "Some plant msg") -> None:
        super().__init__(msg)


class WaterError(GardenError):
    def __init__(self, msg: str = "Some water msg") -> None:
        super().__init__(msg)


def maintain(plant: str) -> None:
    if plant != "tomato":
        raise PlantError
    pass


def use_water(capacity: int, use: int) -> None:
    if use > capacity:
        raise WaterError
    pass


def test_exceptions() -> None:
    try:
        maintain("tomato")
        print("No err")
    except GardenError as e:
        print(f"Caught err: {e}")

    try:
        maintain("carrot")
        print("No err")
    except GardenError as e:
        print(f"Caught err: {e}")

    try:
        use_water(100, 20)
        print("No err")
    except GardenError as e:
        print(f"Caught err: {e}")

    try:
        use_water(100, 2000)
        print("No err")
    except GardenError as e:
        print(f"Caught err: {e}")


if __name__ == "__main__":
    test_exceptions()
