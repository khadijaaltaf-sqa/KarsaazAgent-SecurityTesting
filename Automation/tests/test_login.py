import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

@pytest.fixture
def login_page(page):
    lp = LoginPage(page)
    lp.navigate_login()
    return lp

def test_L01_login_page_elements_present(login_page):
    assert login_page.is_visible(login_page.LOGO)
    assert login_page.is_visible(login_page.USERNAME_INPUT)
    assert login_page.is_visible(login_page.PASSWORD_INPUT)
    assert login_page.is_visible(login_page.LOGIN_SUBMIT_BUTTON)
    assert login_page.is_visible(login_page.FORGOT_PASSWORD_LINK)
    assert login_page.is_visible(login_page.REGISTER_LINK)

def test_L02_username_input(login_page):
    login_page.fill(login_page.USERNAME_INPUT, "testuser")
    assert login_page.page.locator(login_page.USERNAME_INPUT).input_value() == "testuser"

def test_L03_empty_username(login_page):
    login_page.fill(login_page.PASSWORD_INPUT, "password")
    login_page.click(login_page.LOGIN_SUBMIT_BUTTON)
    # Check for validation error or still on login page
    assert "login" in login_page.page.url

def test_L07_successful_login(login_page):
    dashboard = DashboardPage(login_page.page)
    login_page.login("valid_user", "valid_password")
    assert "dashboard" in login_page.page.url
    assert dashboard.is_dashboard_visible()

def test_L11_forgot_password_navigation(login_page):
    login_page.click(login_page.FORGOT_PASSWORD_LINK)
    assert "forgot" in login_page.page.url or "reset" in login_page.page.url

def test_L14_security_sqli_prevention(login_page):
    login_page.login("' OR 1=1 --", "anything")
    assert login_page.is_visible(login_page.ERROR_MESSAGE) or "login" in login_page.page.url
