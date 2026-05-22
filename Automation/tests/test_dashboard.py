import pytest
from pages.dashboard_page import DashboardPage

def test_dashboard_unauthorized_access(page):
    # Try to access dashboard directly without login
    page.goto("https://karsaazagent.com/dashboard")
    
    # Should redirect to login
    assert "login" in page.url

def test_logout_functionality(page):
    # This test assumes a logged in state, which might need a fixture
    # For now, placeholder for the flow
    dashboard_page = DashboardPage(page)
    # login logic would go here...
    
    # dashboard_page.logout()
    # assert "login" in page.url
    pass
