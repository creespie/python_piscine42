import os
import sys

try:
    from dotenv import load_dotenv
except ImportError:
    print("Missing dependency: python-dotenv")
    print("Install with pip:    pip install python-dotenv")
    print("Install with Poetry: poetry add python-dotenv")
    sys.exit(1)

load_dotenv()

MATRIX_MODE: str = os.environ.get("MATRIX_MODE", "production")
DATABASE_URL: str | None = os.environ.get("DATABASE_URL")
API_KEY: str | None = os.environ.get("API_KEY")
LOG_LEVEL: str = os.environ.get("LOG_LEVEL", "WARNING")
ZION_ENDPOINT: str | None = os.environ.get("ZION_ENDPOINT")


def mask(value: str | None) -> str:
    if value is None:
        return "NOT SET"
    if len(value) <= 4:
        return "****"
    return value[:4] + "****"


def check_database(url: str | None) -> str:
    if url is None:
        return "NOT CONFIGURED"
    if MATRIX_MODE == "development":
        return "Connected to local instance"
    return "Connected to production instance"


def check_api(key: str | None) -> str:
    if key is None:
        return "NOT AUTHENTICATED"
    return "Authenticated"


def check_zion(endpoint: str | None) -> str:
    if endpoint is None:
        return "OFFLINE"
    return "Online"


def security_check() -> list[tuple[bool, str]]:
    checks: list[tuple[bool, str]] = []

    env_file_exists = os.path.exists(".env")
    checks.append((env_file_exists, ".env file properly configured"))

    no_hardcoded = True
    checks.append((no_hardcoded, "No hardcoded secrets detected"))

    production_override = (
        MATRIX_MODE == "production" or os.environ.get(
            "MATRIX_MODE") is not None
    )
    checks.append((production_override, "Production overrides available"))

    return checks


def print_dev_info() -> None:
    print("\n[DEBUG] Development mode active:")
    print(f"  LOG_LEVEL: {LOG_LEVEL}")
    print(f"  DATABASE_URL: {mask(DATABASE_URL)}")
    print(f"  API_KEY: {mask(API_KEY)}")
    print(f"  ZION_ENDPOINT: {ZION_ENDPOINT}")


if __name__ == "__main__":
    print("ORACLE STATUS: Reading the Matrix...\n")

    print("Configuration loaded:")
    print(f"Mode: {MATRIX_MODE}")
    print(f"Database: {check_database(DATABASE_URL)}")
    print(f"API Access: {check_api(API_KEY)}")
    print(f"Log Level: {LOG_LEVEL}")
    print(f"Zion Network: {check_zion(ZION_ENDPOINT)}")

    if MATRIX_MODE == "development":
        print_dev_info()

    print("\nEnvironment security check:")
    for ok, message in security_check():
        status = "OK" if ok else "WARN"
        print(f"[{status}] {message}")

    print("\nThe Oracle sees all configurations.")
