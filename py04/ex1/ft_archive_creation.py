import sys
from typing import IO


def transform(content: str) -> str:
    lines = content.splitlines()
    return "".join(line + "#\n" for line in lines)


def save(content: str) -> None:
    try:
        name: str = input("Enter new file name (or empty): ")
    except (KeyboardInterrupt, EOFError):
        print("\nProgram interrupted by user.")
        return

    if name == "":
        print("Not saving data.")
        return

    print(f"Saving data to '{name}'")
    try:
        out: IO = open(name, "w")
    except OSError as e:
        print(f"Error opening file '{name}': {e}")
        print("Data not saved.")
        return

    try:
        out.write(content)
    except OSError as e:
        print(f"Error writing file '{name}': {e}")
        print("Data not saved.")
        return
    finally:
        out.close()

    print(f"Data saved in file '{name}'.")


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_archive_creation.py <file>")
        return

    name: str = sys.argv[1]
    print("=== Cyber Archives Recovery & Preservation ===")
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

    new_content: str = transform(content)
    print("Transform data:")
    print("---")
    print(new_content, end="" if new_content.endswith("\n") else "\n")
    print("---")

    save(new_content)


if __name__ == "__main__":
    main()
