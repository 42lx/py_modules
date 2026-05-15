import sys


def main() -> None:
    lst = []
    for arg in sys.argv[1:]:
        try:
            lst.append(int(arg))
        except ValueError:
            print(f"Invalid param {arg}")
    if len(lst) == 0:
        print("No args provided")
        return
    print("Args provided:", lst)
    print("Max arg:", max(lst))
    print("Min arg:", min(lst))
    print("Average:", sum(lst) / len(lst))


if __name__ == "__main__":
    main()
