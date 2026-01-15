# Selenium Python Project - OrangeHRM Automation

## Overview
This is an automated testing project using Selenium WebDriver with Python to test the OrangeHRM demo application. The project implements the Page Object Model (POM) design pattern for maintainable and scalable test automation.

**Test Application:** [OrangeHRM Demo](https://opensource-demo.orangehrmlive.com)  
**Tester:** Mike EJ Redondo

## Project Structure
```
.
├── pages/                      # Page Object Model classes
│   ├── base_page.py           # Base class with common Selenium operations
│   ├── login_page.py          # Login page specific operations
│   └── __pycache__/
├── test/                       # Test files
│   ├── test_login.py          # Login test cases
│   └── __pycache__/
├── data_files/                # Test data files
├── output/                    # Test output and reports
├── conftest.py               # Pytest fixtures and configurations
├── tc.py                     # Test configuration or utilities
├── 1.js                      # JavaScript file
├── guide.txt                 # Setup guide
└── README.md                 # This file
```

## Setup Instructions
1. **Create a Virtual Environment**  
   Run the following command to create a virtual environment:
   ```bash
   python -m venv venv
   ```

2. **Activate the Virtual Environment**  
   For Windows:
   ```bash
   venv\Scripts\activate
   ```

3. **Install Dependencies**  
   Install the required packages using pip:
   ```bash
   pip install selenium pytest webdriver-manager
   ```

4. **Freeze Requirements**  
   To create a `requirements.txt` file with the installed packages, run:
   ```bash
   pip freeze > requirements.txt
   ```

## Running Tests
Execute tests using pytest:
```bash
pytest test/
```

To run tests with HTML report:
```bash
pytest test/ --html=output/report.html
```

## Git Management
- To move the `.git` directory to the root directory:
  ```powershell
  Move-Item "selenium-python\.git" ".\"
  ```

- To check the branches:
  ```powershell
  git branch -a
  ```

- To remove the cloned repository files:
  ```powershell
  Remove-Item "selenium-python" -Recurse -Force
  ```

## Project Components

### Pages (Page Object Model)
- **base_page.py**: Base class containing reusable Selenium operations
  - `open(url)` - Navigate to a URL
  - `find_element(locator)` - Find element with explicit wait
  - `type(locator, text, clear)` - Type text into an element
  - `click(locator)` - Click an element

- **login_page.py**: Login page operations inheriting from BasePage
  - `type_login_credentials(username, password)` - Login with credentials
  - `goto_dashboard()` - Verify dashboard navigation
  - `get_invalid_credential()` - Get invalid credential error message
  - `get_required_field()` - Get required field error message
  - `log_out()` - Logout from application

### Tests
- **test_login.py**: Login test cases
  - `test_emptyfields_credentials()` - Test empty field validation
  - Additional tests for valid and invalid credentials (commented out)

### Configuration
- **conftest.py**: Pytest configuration
  - Chrome WebDriver fixture with automatic driver management
  - Screenshot capture on test failure
  - HTML report metadata configuration

## Notes
- Ensure that you have Python and pip installed on your system before setting up the project.
- The project uses `webdriver-manager` to automatically manage ChromeDriver versions
- Screenshots are automatically saved in the `screenshots/` folder when tests fail
- Test reports are generated in HTML format in the `output/` folder
