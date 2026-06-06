import os
import site
import sys


def in_virtual_env() -> bool:
    return sys.base_prefix != sys.prefix


def venv_name() -> str:
    venv_path = os.environ.get("VIRTUAL_ENV") or sys.prefix
    return os.path.basename(os.path.normpath(venv_path))


def site_packages_path() -> str:
    for path in site.getsitepackages():
        if "site-packages" in path:
            return path
    return site.getusersitepackages()


def report_inside_venv() -> None:
    venv_path = os.environ.get("VIRTUAL_ENV") or sys.prefix
    print("MATRIX STATUS: Welcome to the construct")
    print()
    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {venv_name()}")
    print(f"Environment Path: {venv_path}")
    print()
    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting")
    print("the global system.")
    print()
    print("Package installation path:")
    print(site_packages_path())


def report_outside_venv() -> None:
    print("MATRIX STATUS: You're still plugged in")
    print()
    print(f"Current Python: {sys.executable}")
    print("Virtual Environment: None detected")
    print()
    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.")
    print()
    print("To enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate # On Unix")
    print("matrix_env\\Scripts\\activate # On Windows")
    print()
    print("Then run this program again.")


def main() -> None:
    try:
        if in_virtual_env():
            report_inside_venv()
        else:
            report_outside_venv()
    except OSError as exc:
        print(f"Error inspecting environment: {exc}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
