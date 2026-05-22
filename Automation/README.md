# Karsaaz Agent Automation Suite

This project contains an automated testing suite for [karsaazagent.com](https://karsaazagent.com) built with Python and Playwright.

## Prerequisites
- Python 3.8+
- [Playwright](https://playwright.dev/python/)

## Installation
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Install browser drivers:
   ```bash
   playwright install
   ```

## Project Structure
- `pages/`: Page Object Model (POM) classes.
- `tests/`: Test cases for different modules.
- `conftest.py`: Fixtures and configuration.

## Running Tests
Run all tests:
```bash
pytest
```

Run tests with browser visible:
```bash
pytest --headed
```

## Important Note on Selectors
The current scripts use **placeholder selectors** (e.g., `#username`, `.login-btn`). Since the agent could not access the live DOM, you **must** update these in the `pages/` files with the actual element IDs or classes from the website.

### Files to Update:
- [landing_page.py](file:///e:/security%20Testing/Karsaaz%20Agent/Automation/pages/landing_page.py)
- [login_page.py](file:///e:/security%20Testing/Karsaaz%20Agent/Automation/pages/login_page.py)
- [register_page.py](file:///e:/security%20Testing/Karsaaz%20Agent/Automation/pages/register_page.py)
- [dashboard_page.py](file:///e:/security%20Testing/Karsaaz%20Agent/Automation/pages/dashboard_page.py)
