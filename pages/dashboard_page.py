# 1 import what we need
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

# 2 define dashboard page class
class DashboardPage(BasePage):

    # 3 set locators (elements unique to dashboard)
    HEADER = (By.CSS_SELECTOR, "h6.oxd-text")
    USER_DROPDOWN = (By.CLASS_NAME, "oxd-userdropdown-name")
    LOGOUT_BTN = (By.XPATH, "//a[text()='Logout']")

    # 4 set functions (dashboard actions)
    def is_loaded(self):
        return self.is_visible(self.HEADER)

    def logout(self):
        self.click(self.USER_DROPDOWN)
        self.click(self.LOGOUT_BTN)
