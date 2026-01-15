from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
    
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
        return self.find_element(locator).click()