# Selenium Imports
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from drivers.chrome.chrome_driver import driver

import pandas as pd

# Constants
from Constants.LoginModule import LoginElements
from Constants.ConfigFiles import LoginConfig, UrlConfig

from Input.InputReader import InputReader
import logging

log = logging.getLogger(__name__)

class LoginPage:

    url = None
    ip_username = None
    ip_password = None
    btn_submmit = None

    username = None
    password = None

    ip_username_found = False
    ip_password_found = False
    btn_submmit_found = False

    def __init__(self, file_path):
        try:
            self.file_path = file_path
            self.config_data = InputReader(self.file_path, UrlConfig.CONFIG_SHEET_NAME)
            self.input_data = InputReader(self.file_path, LoginConfig.CONFIG_SHEET_NAME)
            self.setup_urls()
        except Exception as e:
            log.error(f"LoginPage > setup : {e}")

    def setup_urls(self):
        try:
            data = self.config_data.getInputData()
            for index, row in data.iterrows():
                if row['Module'] == LoginElements.MODULE:
                    self.url = row['URL']
                    break
                return
        except Exception as e:
            log.error(f"LoginPage > setup_urls : {e}")

    def setup_elements(self):
        try:
            data = self.input_data.getInputData()
            elements = data[data.is_input == 'Y']
            for index, row in data.iterrows():
                element = row['element']
                if element == LoginElements.USERNAME:
                    self.ip_username = driver.find_element(By.XPATH,row['xpath'])
                    self.ip_username_found = True
                elif element == LoginElements.PASSWORD:
                    self.ip_password = driver.find_element(By.XPATH,row['xpath'])
                    self.ip_password_found = True
                elif element == LoginElements.SUBMIT:
                    self.btn_submmit = driver.find_element(By.XPATH,row['xpath'])
                    self.btn_submmit_found = True

            if (self.ip_username_found and self.ip_password_found and self.btn_submmit_found):
                self.get_input_data(elements)
        except Exception as e:
            log.error(f"LoginPage > setup_elements > {e}")

    def get_input_data(self, elements):
        try:
            for index, row in elements.iterrows():
                element = row['element']
                if element == LoginElements.USERNAME:
                    self.username = row['value']
                elif element == LoginElements.PASSWORD:
                    self.password = row['value']
        except Exception as e:
            log.error(f"LoginPage > get_input_data > {e}")

    def performLogin(self):
        try:
            driver.get(self.url)
            
            driver.maximize_window()

            self.setup_elements()

            self.clearInputData()

            self.ip_username.send_keys(self.username)
            self.ip_password.send_keys(self.password)
            self.btn_submmit.click()

        except Exception as e:
            log.error(f"LoginPage > performLogin > {e}")

    def clearInputData(self):
        try:
            self.ip_username.clear()            
            self.ip_password.clear()
        except Exception as e:
            log.error(f"LoginPage > clearInputData > {e}")