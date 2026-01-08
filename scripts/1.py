from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

def setup_driver(url=URL):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(3)
    driver.get(url)
    return driver

def teardown_driver(driver):
    driver.quit()

def wait_for_element(driver, by, value, timeout=10):
    return WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((by, value))
    )

def login(driver, username_str, password_str):
    wait_for_element(driver, By.NAME, "username").send_keys(username_str)
    driver.find_element(By.NAME, "password").send_keys(password_str)
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()


def assert_login_result(driver):
    wait = WebDriverWait(driver, 10)

    result = wait.until(
        EC.any_of(
            EC.presence_of_element_located(
                (By.XPATH, "//h6[text()='Dashboard']")
            ),
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, ".oxd-alert-content-text")
            )
        )
    )

    # SUCCESS case
    if result.text == "Dashboard":
        assert True

    # FAILURE case
    else:
        assert "Invalid credentials" in result.text

def test_login_success():
    driver = setup_driver()
    login(driver, "Admin", "admin123")
    assert assert_login_result(driver) is True
    teardown_driver(driver)

def test_login_failure():
    driver = setup_driver()
    login(driver, "wrong_user", "wrong_pass")
    assert assert_login_result(driver) is False
    teardown_driver(driver)
