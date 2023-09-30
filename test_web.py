from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import pytest
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("test_web")

def test_web():
    service = Service()
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    try:
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.set_window_size(width=1920, height=1080)
        driver.maximize_window()
        driver.get("https://appworks.tw")

        # Add your test assertions or interactions here
        logger.info(f"Chrome version: {driver.capabilities['version']}")
        logger.info(f"ChromeDriver version: {driver.capabilities['chrome']['chromedriverVersion']}")
        assert "By Founders, For Founders" in driver.title  # Example assertion for the page title
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")
    finally:
        if 'driver' in locals() and driver is not None:
            driver.quit()

# Run the test
test_web()
