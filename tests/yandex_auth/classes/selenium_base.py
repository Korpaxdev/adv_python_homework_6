from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait


class SeleniumBase:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find_element(self, by: By, selector: str, timeout: int = 3) -> WebElement | None:
        elem = None
        try:
            elem = WebDriverWait(self.driver, timeout=timeout).until(lambda d: d.find_element(by=by, value=selector))
        finally:
            return elem

    def find_elements(self, by: By, selector: str, timeout: int = 3) -> list[WebElement] | None:
        elements = None
        try:
            elements = WebDriverWait(self.driver, timeout=timeout).until(
                lambda d: d.find_elements(by=by, value=selector))
        finally:
            return elements
