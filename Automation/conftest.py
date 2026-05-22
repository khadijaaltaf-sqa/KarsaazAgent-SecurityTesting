import pytest
from playwright.sync_api import sync_playwright
import os

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {
            "width": 1920,
            "height": 1080,
        },
    }

@pytest.fixture(scope="function")
def page(context):
    page = context.new_page()
    yield page
    page.close()

# Hook to add environment info to the report if using pytest-html or similar
def pytest_configure(config):
    config.addinivalue_line(
        "markers", "smoke: check basic functionality"
    )
    config.addinivalue_line(
        "markers", "regression: check all functionality"
    )
