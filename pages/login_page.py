#1 import what we need
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
#2 defined login page class
class LoginPage(BasePage):
#3 set locators
    USERNAME_place = (By.CSS_SELECTOR, "label.oxd-label")
    USERNAME = (By.NAME, "username")
    PASSWORD = (By.NAME, "password")
    LOGIN_BTN = (By.CSS_SELECTOR, "button[type='submit']")
    DASHBOARD_HEADER = (By.CSS_SELECTOR, "h6.oxd-text")

#4 set function
    def login(self, username, password):
        self.find_element(self.USERNAME)
        self.find_element(self.PASSWORD)
        self.type(self.USERNAME,username)
        self.type(self.PASSWORD,password)
        self.click(self.LOGIN_BTN)