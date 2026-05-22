from playwright.sync_api import Page, Locator

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self, url: str):
        """Navigate to a URL."""
        self.page.goto(url)

    def get_title(self) -> str:
        """Get the page title."""
        return self.page.title()

    def wait_for_url(self, url_pattern: str):
        """Wait for the URL to match a pattern."""
        self.page.wait_for_url(url_pattern)

    def click(self, selector: str):
        """Click an element."""
        self.page.click(selector)

    def fill(self, selector: str, text: str):
        """Fill an input field."""
        self.page.fill(selector, text)

    def get_text(self, selector: str) -> str:
        """Get text content of an element."""
        return self.page.inner_text(selector)
    
    def is_visible(self, selector: str) -> bool:
        """Check if element is visible."""
        return self.page.is_visible(selector)
