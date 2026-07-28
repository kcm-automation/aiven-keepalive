import logging
from playwright.sync_api import sync_playwright
import random

def aaa():
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False)
        page = browser.new_page()

        logging.info("Going to example.com...")
        page.goto("https://example.com")
        browser.close()
