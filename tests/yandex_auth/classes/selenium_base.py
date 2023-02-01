from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait


class SeleniumBase:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find_element(self, by: By, selector: str, timeout: int | float = 1.5) -> WebElement | None:
        """
        В течении timeout дожидается, когда появился элемент с selector на страницы.
        В случае истечения timeout, возвращает None
        :params
        - by - Класс webdriver.common.by. Определяет как искать элемент
        - selector - str. Селектор элемента
        - timeout - int or float. Значение timeout, в течении которого driver дожидается элемента
        """
        elem = None
        try:
            elem = WebDriverWait(self.driver, timeout=timeout, poll_frequency=0.3).until(
                lambda d: d.find_element(by=by, value=selector))
        finally:
            return elem

    def find_elements(self, by: By, selector: str, timeout: int | float = 1.5) -> list[WebElement] | None:
        """
                В течении timeout дожидается, когда появился элементы с selector на страницы.
                В случае истечения timeout, возвращает None
                :params
                - by - Класс webdriver.common.by. Определяет как искать элементы
                - selector - str. Селектор элементов
                - timeout - int or float. Значение timeout, в течении которого driver дожидается элементов
                """
        elements = None
        try:
            elements = WebDriverWait(self.driver, timeout=timeout, poll_frequency=0.3).until(
                lambda d: d.find_elements(by=by, value=selector))
        finally:
            return elements
