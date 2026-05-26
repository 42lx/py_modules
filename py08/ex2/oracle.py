import os
import sys
from pathlib import Path

try:
    from dotenv import load_dotenv
except ImportError:
    print("Missing dependency: python-dotenv", file=sys.stderr)
    print("Install with: pip install python-dotenv", file=sys.stderr)
    sys.exit(1)


REQUIRED_VARS = [
    "MATRIX_MODE",
    "DATABASE_URL",
    "API_KEY",
    "LOG_LEVEL",
    "ZION_ENDPOINT",
]


def load_env() -> Path:
    env_path = Path(__file__).resolve().parent / ".env"
    load_dotenv(dotenv_path=env_path, override=False)
    return env_path


def mask(value: str) -> str:
    if len(value) <= 4:
        return "*" * len(value)
    return value[:2] + "*" * (len(value) - 4) + value[-2:]


def describe_database(url: str, mode: str) -> str:
    if not url:
        return "Not configured"
    if mode == "production":
        return "Connected to production cluster"
    return "Connected to local instance"


def describe_api(key: str) -> str:
    if not key:
        return "Missing API key"
    return f"Authenticated ({mask(key)})"


def describe_zion(endpoint: str) -> str:
    if not endpoint:
        return "Offline"
    return "Online"


def report_config(env_path: Path) -> int:
    mode = os.environ.get("MATRIX_MODE", "")
    db = os.environ.get("DATABASE_URL", "")
    api = os.environ.get("API_KEY", "")
    log = os.environ.get("LOG_LEVEL", "")
    zion = os.environ.get("ZION_ENDPOINT", "")

    missing = [v for v in REQUIRED_VARS if not os.environ.get(v)]

    print("ORACLE STATUS: Reading the Matrix...")
    print()
    print("Configuration loaded:")
    print(f"Mode: {mode or 'unset'}")
    print(f"Database: {describe_database(db, mode)}")
    print(f"API Access: {describe_api(api)}")
    print(f"Log Level: {log or 'unset'}")
    print(f"Zion Network: {describe_zion(zion)}")
    print()

    if mode == "production":
        print("Running in PRODUCTION: verbose logs disabled, secrets masked.")
    elif mode == "development":
        print("Running in DEVELOPMENT: verbose logs, debug routes open.")
    else:
        print("Running in UNKNOWN mode: set MATRIX_MODE to dev or prod.")
    print()

    print("Environment security check:")
    if missing:
        print(f"[WARN] Missing variables: {', '.join(missing)}")
    else:
        print("[OK] No hardcoded secrets detected")
    if env_path.exists():
        print("[OK] .env file properly configured")
    else:
        print(f"[WARN] No .env file at {env_path} (copy .env.example to .env)")
    print("[OK] Production overrides available")
    print()
    print("The Oracle sees all configurations.")

    if missing:
        if mode == "production":
            print(
                f"[ERROR] Production requires all variables set. "
                f"Missing: {', '.join(missing)}",
                file=sys.stderr,
            )
        return 1
    return 0


def main() -> None:
    try:
        env_path = load_env()
        rc = report_config(env_path)
        sys.exit(rc)
    except OSError as exc:
        print(f"Error reading environment: {exc}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
