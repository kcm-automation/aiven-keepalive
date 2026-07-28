import logging
from playwright.sync_api import sync_playwright
import random

def check_aiven_service(aiven_username: str, aiven_password: str) -> None:
    # set up jitters
    after_clicking_accept   = random.randrange(500,1000)
    after_entering_email    = random.randrange(500,1000)
    after_clicking_login_1  = random.randrange(500,3000)
    after_entering_password = random.randrange(1000,3000)
    to_close                = random.randrange(1000, 3000)

    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False)
        page = browser.new_page()

        logging.info("Going to example.com...")
        page.goto("https://example.com")

        logging.debug("Waiting 3 seconds...")
        page.wait_for_timeout(3000)

        logging.info("Going to aiven login page...")
        page.goto("https://console.aiven.io/login", wait_until="networkidle")

        logging.debug("Clicking ok to accept cookies")
        page.click('button:has-text("Accept")')
        page.wait_for_timeout(after_clicking_accept)

        logging.info("Typing in login details...")

        logging.debug("Typing in email field...")
        page.fill('input[name="email"]', aiven_username)
        page.wait_for_timeout(after_entering_email)

        logging.debug("Clicking login button (to enter password next)")
        page.click('button[type="submit"]:has-text("Log in")')
        page.wait_for_timeout(after_clicking_login_1)

        logging.debug("Typing in password...")
        page.fill('input[type="password"]', aiven_password)
        page.wait_for_timeout(after_entering_password)

        logging.debug("Clicking login button...")
        page.click('button[type="submit"]:has-text("Log in")')

        logging.info("Logging in...")
        page.wait_for_timeout(1000)

        logging.debug("Checking service status")
        status_span = page.locator('span.Aquarium-StatusChip')
        status_text = status_span.text_content().strip()

        if status_text == "Powered off":
            logging.critical("⚠️ Service is powered off.")

            logging.debug("Closing browser...")
            page.wait_for_timeout(to_close)
            browser.close()
            return None

        logging.info("🟢 Service is running")
        page.wait_for_timeout(to_close)
        browser.close()

    return None
