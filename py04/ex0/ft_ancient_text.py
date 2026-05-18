import sys
from typing import IO


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return

    name: str = sys.argv[1]
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{name}'")

    try:
        f: IO = open(name, "r")
    except OSError as e:
        print(f"Error opening file '{name}': {e}")
        return

    try:
        content: str = f.read()
        print("---")
        print(content, end="" if content.endswith("\n") else "\n")
        print("---")
    except OSError as e:
        print(f"Error reading file '{name}': {e}")
        return
    finally:
        f.close()
        print(f"File '{name}' closed.")


if __name__ == "__main__":
    main()
