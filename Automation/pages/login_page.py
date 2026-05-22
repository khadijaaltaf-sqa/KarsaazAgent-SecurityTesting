from pages.base_page import BasePage

class LoginPage(BasePage):
    URL = "https://karsaazagent.com/login"
    
    # Selectors (Placeholders)
    USERNAME_INPUT = "#username"
    PASSWORD_INPUT = "#password"
    LOGIN_SUBMIT_BUTTON = "button[type='submit']"
    REMEMBER_ME_CHECKBOX = "#remember_me"
    FORGOT_PASSWORD_LINK = "text=Forgot Password"
    REGISTER_LINK = "text=Register now"
    ERROR_MESSAGE = ".alert-danger"
    LOGO = ".logo-brand"

    def navigate_login(self):
        self.navigate(self.URL)

    def login(self, username, password):
        self.fill(self.USERNAME_INPUT, username)
        self.fill(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_SUBMIT_BUTTON)

    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)
