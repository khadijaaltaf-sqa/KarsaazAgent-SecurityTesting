import pytest
from pages.register_page import RegisterPage

@pytest.fixture
def register_page(page):
    rp = RegisterPage(page)
    rp.navigate_register()
    return rp

def test_R01_register_page_elements_present(register_page):
    assert register_page.is_visible(register_page.FULL_NAME_INPUT)
    assert register_page.is_visible(register_page.EMAIL_INPUT)
    assert register_page.is_visible(register_page.PASSWORD_INPUT)
    assert register_page.is_visible(register_page.CONFIRM_PASSWORD_INPUT)
    assert register_page.is_visible(register_page.TERMS_CHECKBOX)
    assert register_page.is_visible(register_page.REGISTER_SUBMIT_BUTTON)

def test_R04_email_validation(register_page):
    register_page.register("Test", "invalid-email", "Pass123!", "Pass123!")
    # Check for error or still on register page
    assert register_page.is_visible(register_page.ERROR_MESSAGE) or "register" in register_page.page.url

def test_R07_password_mismatch(register_page):
    register_page.register("Test", "test@test.com", "Pass123!", "Pass456!")
    assert register_page.is_visible(register_page.ERROR_MESSAGE) or "register" in register_page.page.url

def test_R11_login_link_navigation(register_page):
    register_page.click(register_page.LOGIN_LINK)
    assert "login" in register_page.page.url
