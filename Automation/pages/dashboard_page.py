from pages.base_page import BasePage

class DashboardPage(BasePage):
    # Base URL pattern for dashboard
    URL_PATTERN = "**/dashboard"
    
    # Selectors (Placeholders)
    WELCOME_MESSAGE = "h1.welcome-text"
    LOGOUT_BUTTON = ".logout-link"
    USER_PROFILE_ICON = ".profile-icon"

    def is_dashboard_visible(self):
        return self.is_visible(self.WELCOME_MESSAGE)

    def logout(self):
        self.click(self.LOGOUT_BUTTON)
