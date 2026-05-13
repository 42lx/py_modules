def input_temperature(temp_str: str) -> int:
    res: int = int(temp_str)
    if (not (res >= 0 and res <= 40)):
        raise ValueError(f'Temperature {res} is in invalid range')
    return res


def test_temperature() -> None:
    try:
        res: int = input_temperature("25")
        print(f"Temperature is now {res}°C")
    except Exception as e:
        print(f"Caught input_temperature err: {e}")

    try:
        res = input_temperature("abc")
        print(f"Temperature is now {res}°C")
    except Exception as e:
        print(f"Caught input_temperature err: {e}")

    try:
        res = input_temperature("100")
        print(f"Temperature is now {res}°C")
    except Exception as e:
        print(f"Caught input_temperature err: {e}")

    try:
        res = input_temperature("-50")
        print(f"Temperature is now {res}°C")
    except Exception as e:
        print(f"Caught input_temperature err: {e}")


if __name__ == "__main__":
    test_temperature()
