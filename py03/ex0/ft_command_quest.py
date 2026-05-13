import sys


def main() -> None:
    i: int = 0
    for arg in sys.argv:
        if i == 0:
            print("program name:", arg)
        else:
            print(f"Arg {i}:", arg)
        i += 1
    print("Total args:", len(sys.argv))


if __name__ == "__main__":
    main()
