import pytest
from pages.landing_page import LandingPage

@pytest.fixture
def landing_page(page):
    lp = LandingPage(page)
    lp.navigate_home()
    return lp

def test_H01_logo_click(landing_page):
    landing_page.click(landing_page.LOGO)
    assert landing_page.page.url.rstrip("/") == landing_page.URL.rstrip("/")

def test_H03_login_nav(landing_page):
    landing_page.click(landing_page.LOGIN_BUTTON)
    assert "login" in landing_page.page.url

def test_H08_footer_social_presence(landing_page):
    # Verify at least one social link is present
    assert landing_page.page.locator(landing_page.FOOTER_SOCIAL).count() > 0

def test_H10_mobile_responsive_menu(page):
    # Resize to mobile
    page.set_viewport_size({"width": 375, "height": 812})
    landing_page = LandingPage(page)
    landing_page.navigate_home()
    assert landing_page.is_visible(landing_page.MOBILE_MENU_TOGGLE)
