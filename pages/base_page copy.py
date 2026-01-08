# 1 import what we need 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 2 defined basepage class
class BasePage:
# 3 create constructor
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver,timeout)
    
# 4 find element
    def open(self, url):
        return self.driver.get(url)

    def find_elements(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def type(self,locator,text,clear=True):
        element = self.find_elements(locator)
        if clear:
            element.clear()
        element.send_keys(text)

# 5
# 6
# 7
# 8