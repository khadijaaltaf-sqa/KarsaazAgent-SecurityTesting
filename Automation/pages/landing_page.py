from pages.base_page import BasePage

class LandingPage(BasePage):
    URL = "https://karsaazagent.com"
    
    # Selectors (Placeholders)
    NAV_LINKS = "nav a"
    FEATURES_LINK = "text=Features"
    PRICING_LINK = "text=Pricing"
    LOGIN_BUTTON = "text=Login"
    REGISTER_BUTTON = "text=Register"
    LOGO = "img.logo"
    FOOTER_SOCIAL = ".footer-social a"
    LEGAL_LINKS = ".footer-legal a"
    MOBILE_MENU_TOGGLE = ".navbar-toggler"
    HERO_TEXT = "h1.hero-title"

    def navigate_home(self):
        self.navigate(self.URL)

    def click_login(self):
        self.click(self.LOGIN_BUTTON)
    
    def click_register(self):
        self.click(self.REGISTER_BUTTON)
