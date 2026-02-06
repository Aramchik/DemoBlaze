from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.chrome.options import Options

@pytest.fixture()
def browser():
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    options.add_experimental_option('detach', True)
    chrome_browser = webdriver.Chrome(options=options)
    chrome_browser.implicitly_wait(10)
    return chrome_browser
