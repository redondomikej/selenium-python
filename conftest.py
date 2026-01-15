import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# Driver fixture
@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()

# Screenshot hook for pytest-html
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver")
        if driver:
            import pytest_html
            os.makedirs("screenshots", exist_ok=True)
            screenshot_path = f"screenshots/{item.name}.png"
            driver.save_screenshot(screenshot_path)
            if hasattr(rep, "extra"):
                extra = rep.extra
            else:
                extra = []
            extra.append(pytest_html.extras.image(screenshot_path))
            rep.extra = extra

# Add metadata to pytest-html report
def pytest_configure(config):
    if hasattr(config, "_metadata"):
        config._metadata["Project Name"] = "OrangeHRM Automation"
        config._metadata["Tester"] = "Mike EJ Redondo"
        config._metadata["URL"] = "https://opensource-demo.orangehrmlive.com"
