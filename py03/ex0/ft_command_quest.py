import sys


def main() -> None:
    i: int = 0
    for arg in sys.argv:
        if i == 0:
            print("program name:", arg)
        else:
            print(f"Arg {i}:", arg)
        i += 1
    if i == 1:
        print("No args provided")
    print("Total args:", len(sys.argv))


if __name__ == "__main__":
    main()
