# first_script.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# def test_open_orangehrm():
#     # Initialize Chrome dynamically
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
#     driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    
#     # Wait 5 seconds to see the page
#     time.sleep(5)
    
#     driver.quit()

def setup():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(10)  # wait for elements
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    return driver
def teardown(driver):
    driver.quit()
def test_web():
    driver = setup()

    title = driver.title
    assert title == "OrangeHRM"

    username = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "username"))
)
    username.send_keys("Admin")

    password = driver.find_element(By.NAME, "password")
    password.send_keys("admi123")

    login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    login_button.click()

    time.sleep(5) 

    teardown(driver)