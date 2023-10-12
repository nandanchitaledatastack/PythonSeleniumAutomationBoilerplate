import logging

log = logging.getLogger(__name__)

def get_web_element(driver, By_type, value):
    try:
        return driver.find_element(By_type,value)
    except Exception as e:
        log.error(f"CommonOperations > get_web_element > {e}")