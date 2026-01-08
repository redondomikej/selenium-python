#1 import what we need
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import time
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

#2 setup driver using pytest annotation
@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    time.sleep(5)
    driver.quit()
#3 set test scenario
def test_login(driver):
    login = LoginPage(driver)
    login.open("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    login.login("admin","admin123")
    # assert login.is_visible(LoginPage.DASHBOARD_HEADER), "OrangeHRM"
    dashboard= DashboardPage(driver)
    assert dashboard.is_visible(DashboardPage.HEADER),"OrageHRM"