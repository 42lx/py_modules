import sys


def main() -> None:
    i: int = 0
    for arg in sys.argv:
        if i == 0:
            print("program name:", arg)
        else:
            print(f"Arg {i}:", arg)
        i += 1
    if len(sys.argv) == 1:
        print("No args provided")
    else:
        print("Total args:", len(sys.argv) - 1)


if __name__ == "__main__":
    main()
