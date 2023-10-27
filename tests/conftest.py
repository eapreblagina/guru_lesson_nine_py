import pytest
from selene import browser


@pytest.fixture(scope="function", autouse=True)
def browser_setup():
    browser.config.window_width = 1920
    browser.config.window_height = 1000

    yield

    browser.quit()