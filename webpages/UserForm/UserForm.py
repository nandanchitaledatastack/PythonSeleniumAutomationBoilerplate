# Selenium Imports
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from drivers.chrome.chrome_driver import driver

import time

from elements.get_elements import get_web_element

import pandas as pd

# Constants
from Constants.UserFormModule import UserFormElements
from Constants.ConfigFiles import UserFormConfig, UrlConfig

from Input.InputReader import InputReader
import logging

log = logging.getLogger(__name__)

class UserForm:

    url = None
    ipBusinessName = None
    ipBusinessName = None
    ipFirstName = None
    ipMiddleName = None
    ipLasttName = None
    ipStreet = None
    ipCity = None
    ipState = None
    ipPostalCode = None
    ipCountry = None
    btn_submmit = None

    def __init__(self, file_path):
        try:
            self.file_path = file_path
            self.config_data = InputReader(self.file_path, UrlConfig.CONFIG_SHEET_NAME)
            self.input_data = InputReader(self.file_path, UserFormConfig.CONFIG_SHEET_NAME)
            self.setup_urls()
        except Exception as e:
            log.error(f"UserForm > setup : {e}")

    def setup_urls(self):
        try:
            data = self.config_data.getInputData()
            for index, row in data.iterrows():
                if row['Module'] == UserFormElements.MODULE:
                    self.url = row['URL']
                    break
        except Exception as e:
            log.error(f"UserForm > setup_urls : {e}")

    def setup_elements(self):
        try:
            data = self.input_data.getInputData()
            elements = data[data.is_input == 'Y']
            for index, row in elements.iterrows():
                element = row['element']
                if element == UserFormElements.BUSINESS_NAME:
                    self.ipBusinessName = get_web_element(driver, By.XPATH,row['xpath'] )
                    self.ipBusinessName.send_keys(row['value'])
                elif element == UserFormElements.FIRST_NAME:
                    self.ipFirstName = get_web_element(driver, By.XPATH,row['xpath'] )
                    self.ipFirstName.send_keys(row['value'])
                elif element == UserFormElements.MIDDLE_NAME:
                    self.ipMiddleName = get_web_element(driver, By.XPATH,row['xpath'] )
                    self.ipMiddleName.send_keys(row['value'])
                elif element == UserFormElements.LAST_NAME:
                    self.ipLasttName = get_web_element(driver, By.XPATH,row['xpath'] )     
                    self.ipLasttName.send_keys(row['value'])                   
                elif element == UserFormElements.STREET:
                    self.ipStreet = get_web_element(driver, By.XPATH,row['xpath'] )
                    self.ipStreet.send_keys(row['value'])
                elif element == UserFormElements.CITY:
                    self.ipCity = get_web_element(driver, By.XPATH,row['xpath'] )
                    self.ipCity.send_keys(row['value'])
                elif element == UserFormElements.STATE:
                    self.ipState = get_web_element(driver, By.XPATH,row['xpath'] )
                    self.ipState.send_keys(row['value'])
                elif element == UserFormElements.POSTAL_CODE:
                    self.ipPostalCode = get_web_element(driver, By.XPATH,row['xpath'] )
                    self.ipPostalCode.send_keys(row['value'])
                elif element == UserFormElements.COUNTRY:
                    self.ipCountry = get_web_element(driver, By.XPATH,row['xpath'] )
                    self.ipCountry.send_keys(row['value'])
                elif element == UserFormElements.SUBMIT:
                    self.btn_submmit = get_web_element(driver, By.XPATH,row['xpath'] )

        except Exception as e:
            log.error(f"UserForm > setup_elements > {e}")

    def performAction(self):
        try:
            wait = WebDriverWait(driver, 60)  # Adjust the timeout as needed

            # Wait until the URL matches the target URL
            wait.until(EC.url_to_be(self.url))

            self.setup_elements()
        except Exception as e:
            log.error(f"UserForm > performAction > {e}")