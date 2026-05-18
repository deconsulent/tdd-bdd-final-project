######################################################################
# Behave Environment Setup
######################################################################
"""
Sets up environment for behave tests including Selenium WebDriver.
"""

import os
from selenium import webdriver

WAIT_SECONDS = int(os.environ.get("WAIT_SECONDS", "60"))
BASE_URL = os.environ.get("BASE_URL", "http://localhost:8080")
DRIVER = os.environ.get("DRIVER", "chrome").lower()


def before_all(context):
    """Executed once before all tests"""
    context.base_url = BASE_URL
    context.wait_seconds = WAIT_SECONDS

    if "firefox" in DRIVER:
        context.driver = get_firefox()
    else:
        context.driver = get_chrome()
    context.driver.implicitly_wait(context.wait_seconds)
    context.config.setup_logging()


def after_all(context):
    """Executed once after all tests"""
    context.driver.quit()


def get_chrome():
    """Creates a headless Chrome driver"""
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    return webdriver.Chrome(options=options)


def get_firefox():
    """Creates a headless Firefox driver"""
    options = webdriver.FirefoxOptions()
    options.add_argument("--headless")
    return webdriver.Firefox(options=options)
