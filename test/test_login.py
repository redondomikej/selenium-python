from pages.login_page import LoginPage

# def test_valid_credentials(driver):
#     login = LoginPage(driver)
#     login.open("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
#     login.type_login_credentials("Admin","admin123")
#     get_dashboard = login.goto_dashboard()
#     assert get_dashboard == "Dashboard", f"Expected Dasboard but got, '{get_dashboard}'"
#     login.log_out()

# def test_invalid_credentials(driver):
#     login = LoginPage(driver)
#     login.open("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
#     login.type_login_credentials("Admin","Invalid")
#     get_invalidcred = login.get_invalid_credential()
#     assert get_invalidcred == "Invalid credentials", f"Expected Invalid credentials but got, '{get_invalidcred}'"

def test_emptyfields_credentials(driver):
    login = LoginPage(driver)
    login.open("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    login.type_login_credentials("Admin","")
    get_requiredfield = login.get_required_field()
    assert get_requiredfield == "Requireds", f"Expected Required but got, '{get_requiredfield}'"
