def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        5 / operation_number
    elif operation_number == 1:
        int("abc")
    elif operation_number == 2:
        open("invalidddddd")
    elif operation_number == 3:
        "abc" + 5
    else:
        return

def test_error_types() -> None:
    for i in [0, 1, 2, 3, 4]:
        print(f"Trying op {i}")
        try:
            garden_operations(i)
            print(f"Success {i}")
        except Exception as e:
            print(f"Caught err: {e}")

if __name__ == "__main__":
    test_error_types()
