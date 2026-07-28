from dotenv import load_dotenv
import json
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
    from src.playwright import check_aiven_service

    try:
        json_data = os.environ["AIVEN_SERVICES"]
        logging.debug("envvar AIVEN_SERVICES was found")

    except KeyError:
        err_msg = "Envvar AIVEN_SERVICES was not found"
        logging.critical(err_msg)
        raise RuntimeError(err_msg)

    data = json.loads(json_data)
    for service in data["services"]:
        service_name     = service["service_name"]
        service_email    = service["email_address"]
        service_password = service["password"]

        logging.info(f"Checking service status for {service_name}...")
        check_aiven_service(service_email, service_password)
        logging.info(f"Check for {service_name} complete.")

    logging.info("No more services to check...")

if __name__ == "__main__":
    main()
