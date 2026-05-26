import importlib
import sys
from types import ModuleType


REQUIRED = [
    ("pandas", "Data manipulation"),
    ("numpy", "Numerical computation"),
    ("matplotlib", "Visualization"),
]


def try_import(name: str) -> ModuleType | None:
    try:
        return importlib.import_module(name)
    except ImportError:
        return None


def print_install_instructions(missing: list[str]) -> None:
    print()
    print("Missing dependencies:", ", ".join(missing))
    print()
    print("Install with pip:")
    print("  pip install -r requirements.txt")
    print()
    print("Install with Poetry:")
    print("  poetry install")
    print()
    print("pip vs Poetry:")
    print("  - pip: installs from requirements.txt, no lock file by default")
    print("  - Poetry: uses pyproject.toml + poetry.lock for reproducibility")


def check_dependencies() -> dict[str, ModuleType]:
    loaded: dict[str, ModuleType] = {}
    missing: list[str] = []
    print("Checking dependencies:")
    for name, role in REQUIRED:
        module = try_import(name)
        if module is None:
            print(f"[MISSING] {name} - {role} NOT available")
            missing.append(name)
        else:
            version = getattr(module, "__version__", "unknown")
            loaded[name] = module
            print(f"[OK] {name} ({version}) - {role} ready")
    if missing:
        print_install_instructions(missing)
        sys.exit(1)
    return loaded


def run_analysis(modules: dict[str, ModuleType]) -> None:
    np = modules["numpy"]
    pd = modules["pandas"]
    mpl = modules["matplotlib"]
    mpl.use("Agg")
    plt = importlib.import_module("matplotlib.pyplot")

    print()
    print("Analyzing Matrix data...")
    rng = np.random.default_rng(42)
    n = 1000
    print(f"Processing {n} data points...")
    data = rng.normal(loc=0.0, scale=1.0, size=n)
    df = pd.DataFrame({"value": data})
    df["rolling"] = df["value"].rolling(window=20).mean()

    print("Generating visualization...")
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(df.index, df["value"], color="#00ff41", alpha=0.4, label="raw")
    ax.plot(df.index, df["rolling"], color="#008f11", label="rolling mean")
    ax.set_title("Matrix Data Stream")
    ax.set_xlabel("step")
    ax.set_ylabel("value")
    ax.legend()
    output = "matrix_analysis.png"
    fig.savefig(output, dpi=100)
    plt.close(fig)

    print()
    print("Analysis complete!")
    print(f"Results saved to: {output}")


def main() -> None:
    print("LOADING STATUS: Loading programs...")
    print()
    try:
        modules = check_dependencies()
        run_analysis(modules)
    except (OSError, ValueError) as exc:
        print(f"Error during analysis: {exc}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
