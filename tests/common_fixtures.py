import pytest
from selenium import webdriver


@pytest.fixture
def selenium(selenium):
    selenium.set_window_size(1500, 1100)
    selenium.implicitly_wait(8)

    return selenium


@pytest.fixture
def chrome_options(chrome_options):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--disable-extensions')
    # chrome_options.add_argument('--headless')
    # chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')

    return chrome_options
