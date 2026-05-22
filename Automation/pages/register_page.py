from pages.base_page import BasePage

class RegisterPage(BasePage):
    URL = "https://karsaazagent.com/register"
    
    # Selectors (Placeholders)
    FULL_NAME_INPUT = "#full_name"
    EMAIL_INPUT = "#email"
    PASSWORD_INPUT = "#password"
    CONFIRM_PASSWORD_INPUT = "#confirm_password"
    TERMS_CHECKBOX = "#terms_conditions"
    REGISTER_SUBMIT_BUTTON = "button[type='submit']"
    LOGIN_LINK = "text=Log in"
    ERROR_MESSAGE = ".invalid-feedback"

    def navigate_register(self):
        self.navigate(self.URL)

    def register(self, full_name, email, password, confirm_password):
        self.fill(self.FULL_NAME_INPUT, full_name)
        self.fill(self.EMAIL_INPUT, email)
        self.fill(self.PASSWORD_INPUT, password)
        self.fill(self.CONFIRM_PASSWORD_INPUT, confirm_password)
        self.click(self.REGISTER_SUBMIT_BUTTON)
