import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    chrome_driver = webdriver.Chrome(options=options)
    yield chrome_driver
    chrome_driver.close()

