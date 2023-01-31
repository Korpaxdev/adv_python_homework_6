import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from tests.yandex_auth.classes.selenium_base import SeleniumBase


@pytest.fixture(scope='session')
def get_selenium_base():
    options = Options()
    driver = webdriver.Chrome(options=options)
    yield SeleniumBase(driver)
    driver.quit()
