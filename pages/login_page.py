from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):

    username_el = (By.NAME, "username")
    password_el = (By.NAME, "password")
    loginbtn_el = (By.CSS_SELECTOR, "button.orangehrm-login-button")
    dashboard_el = (By.XPATH, "//h6[contains(@class,'oxd-topbar-header-breadcrumb-module') and text()='Dashboard']")
    invalidcred_el = (By.CSS_SELECTOR, "p.oxd-alert-content-text")
    profile_dropdown_el = (By.CSS_SELECTOR, "span.oxd-userdropdown-tab")
    logout_el = (By.CSS_SELECTOR, "a[href='/web/index.php/auth/logout']")
    required_error_el = (By.CSS_SELECTOR, "span.oxd-input-field-error-message")




    def type_login_credentials(self, username_input, password_input):
        self.type(self.username_el, username_input)
        self.type(self.password_el, password_input)
        self.click(self.loginbtn_el)

    def goto_dashboard(self):
        return self.find_element(self.dashboard_el).text
    
    def get_invalid_credential(self):
        return self.find_element(self.invalidcred_el).text
    
    def get_required_field(self):
        return self.find_element(self.required_error_el).text
    
    def log_out(self):
        self.click(self.profile_dropdown_el)
        self.click(self.logout_el)