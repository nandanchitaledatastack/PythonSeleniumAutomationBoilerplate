"""Contains common settings across the project."""
from logging import INFO
from typing import Optional

from selenium.webdriver.remote.webdriver import WebDriver

import logging

log = logging.getLogger(__name__)

LOGGING_LEVEL = INFO

# Initialize a global driver
driver = None
# : Optional[WebDriver]

# global GLOBAL_DRIVER = None

def set_global_driver(driver: WebDriver):
    """Sets the GLOBAL_DRIVER, so it can be used cross-module.

    Parameters
    ----------
    driver : WebDriver
        The WebDriver whose value is to be saved to GLOBAL_DRIVER. This is currently only done
        from the constructor of the BaseBrowser class.
    """
    # pylint: disable=global-statement
    try:
        global driver
        driver = driver
        if driver is None : raise Exception("Driver object null")
    except Exception as e:
        log.error(f"settings > set_global_driver : {e}")