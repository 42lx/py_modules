class GardenError(Exception):
    def __init__(self, msg: str = "Some garden msg") -> None:
        super().__init__(msg)


class PlantError(GardenError):
    def __init__(self, msg: str = "Some plant msg") -> None:
        super().__init__(msg)


def water_plant(name: str) -> None:
    if name != name.capitalize():
        raise PlantError
    print(f"Watered {name}")


def test_watering_system():
    print("Open system")
    try:
        water_plant("Carrot")
        water_plant("carrot")
    except PlantError:
        print("err")
        return
    finally:
        print("Close system")


if __name__ == "__main__":
    test_watering_system()
