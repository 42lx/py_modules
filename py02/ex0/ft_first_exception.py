def input_temperature(temp_str: str) -> int:
    return int(temp_str)


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


if __name__ == "__main__":
    test_temperature()
