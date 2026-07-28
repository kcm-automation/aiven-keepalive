from dotenv import load_dotenv
import logging
import os

if not os.environ.get("NOT_DOTENV"):
    load_dotenv()
    print(".env was loaded.")

DEFAULT_LOG_LEVEL = "DEBUG"
LOG_LEVEL = os.getenv("LOG_LEVEL", DEFAULT_LOG_LEVEL)
if LOG_LEVEL not in logging._nameToLevel:
    raise RuntimeError(f"Invalid LOG_LEVEL={LOG_LEVEL}")

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=LOG_LEVEL
)

def main():
    print("hello")

if __name__ == "__main__":
    main()
