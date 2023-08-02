"""
This module contains shared fixtures for web UI tests.
"""

import json
import pytest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

CONFIG_PATH = 'config.json'
DEFAULT_WAIT_TIME = 10
SUPPORTED_BROWSERS = ['chrome', 'firefox']


@pytest.fixture(scope='session')
def config():
    # Read the JSON file and return it as a parsed dict
    with open(CONFIG_PATH) as config_file:
        data = json.load(config_file)
    return data


@pytest.fixture(scope='session')
def config_browser(config):
    # Validate and return and return the browser choice from the config data
    if 'browser' not in config:
        raise Exception('The config file does not contain "browser"')
    elif config['browser'] not in SUPPORTED_BROWSERS:
        raise Exception(f'"{config["browser"]}" is not supported browser')
    return config['browser']


@pytest.fixture(scope='session')
def config_wait_time(config):
    # Validate and return the wait time from the config data
    return config['wait_time'] if 'wait_time' in config else DEFAULT_WAIT_TIME


@pytest.fixture
def browser(config_browser, config_wait_time):
    # Initialize WebDriver
    if config_browser == 'chrome':
        driver = webdriver.Chrome()
    elif config_browser == 'firefox':
        driver = webdriver.Firefox()
    else:
        raise Exception(f'"{config_browser}" is not a supported browser')

    # Open browser window to fullscreen
    driver.maximize_window()

    # Wait implicitly for elements to be ready before attempting interaction
    driver.implicitly_wait(config_wait_time)

    # Return the driver object at the end of setup
    yield driver

    # For cleanup, quit the driver
    driver.quit()
