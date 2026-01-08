from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    USERNAME_place = (By.CSS_SELECTOR, "label.oxd-label")
    USERNAME = (By.NAME, "username")
    PASSWORD = (By.NAME, "password")
    LOGIN_BTN = (By.CSS_SELECTOR, "button[type='submit']")
    ERROR_MSG = (By.CSS_SELECTOR, ".oxd-alert-content-text")

    def login(self, username):
        self.find_elements(self.USERNAME)
        self.type(self.USERNAME, username)