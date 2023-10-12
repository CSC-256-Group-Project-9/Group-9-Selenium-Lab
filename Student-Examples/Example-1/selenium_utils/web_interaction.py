# Selenium Lab LLD 2.0

import os
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options


def initialize_driver(browser_type: str) -> WebDriver:
    """
    (LLD 2.1) Initializes the WebDriver based on the browser type provided.
    :param browser_type: browser_type (e.g., 'Chrome', 'Firefox')
    :return: WebDriver instance
    """
    if browser_type == 'Chrome':
        return webdriver.Chrome()
    
    raise ValueError('Driver type not recognized. Supported drivers: "Chrome"')


# LLD does not specify that the webdriver is provided to this function
# but it will likely have to be passed as a parameter, as this function will not have access to it otherwise
# the param if it is needed: "driver: WebDriver" - William
def navigate_to_url(url: str, driver: WebDriver) -> None:
    """
    (LLD 2.2) Uses the WebDriver instance to navigate to the provided URL.
    :param url: url to navigate to
    """
    driver.get(url)
