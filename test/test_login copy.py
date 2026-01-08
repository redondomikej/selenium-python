from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest

from pages.login_page import LoginPage

# Pytest fixture for driver
@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()

# Test Cases
def test_login_valid(driver):
    login = LoginPage(driver)
    login.open("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    login.login("Admin")
    