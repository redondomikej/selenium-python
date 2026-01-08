#1 import what we need
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#2 define basepage class
class BasePage:
#3 set constructor to reuse for whole class
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
#4 set reusble method
    def open(self, url):
        return self.driver.get(url)
    def find_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
    def type(self, locator, text, clear=True):
        element = self.find_element(locator)
        if clear:
            element.clear()
        element.send_keys(text)
    def click(self, locator):
        self.find_element(locator).click()
    def is_visible(self, locator):
        try:
            self.find_element(locator)
            return True
        except:
            return False