import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from tests.yandex_auth.classes.selenium_base import SeleniumBase
from tests.yandex_auth.utils.constatnts import Selectors, Main, ErrorMessages
from typing import TypeVar

Self = TypeVar('Self', bound='AuthPage')


class AuthPage:
    def __init__(self, selenium_base: SeleniumBase, login: str | int, password: str | int):
        self.selenium_base = selenium_base
        self.login = login
        self.password = password
        self.__base_init()

    def validate_email(self) -> Self:
        email_input = self.selenium_base.find_element(By.ID, Selectors.EMAIL_INPUT_ID)
        assert email_input, ErrorMessages.EMAIL_INPUT_NOT_FOUND
        self.__fill_input(email_input, self.login)
        login_hint = self.selenium_base.find_element(By.ID, Selectors.EMAIL_HINT_ID)
        assert not login_hint, login_hint.text
        return self

    def validate_password(self) -> None:
        password_input = self.selenium_base.find_element(By.ID, Selectors.PASSWORD_INPUT_ID)
        if not password_input:
            return self.__check_qr_code()
        self.__fill_input(password_input, self.password)
        password_captcha = self.selenium_base.find_element(By.CLASS_NAME, Selectors.PASSWORD_CAPTCHA_CLASS)
        assert not password_captcha, ErrorMessages.PASSWORD_CAPTCHA
        password_hint = self.selenium_base.find_element(By.ID, Selectors.PASSWORD_HINT_ID)
        assert not password_hint, password_hint.text
        self.__check_phone_number()

    def __check_qr_code(self) -> None:
        self.__wait_for_element_disappeared(Selectors.QR_CODE_CLASS, By.CLASS_NAME, ErrorMessages.QR_CODE)

    def __check_phone_number(self) -> None:
        phone_confirm_button = self.selenium_base.find_element(By.CSS_SELECTOR, Selectors.PHONE_CONFIRM_BUTTON_SELECTOR)
        if phone_confirm_button:
            phone_confirm_button.click()
            self.__wait_for_element_disappeared(Selectors.PHONE_CODE_FIELD_CLASS, By.CLASS_NAME,
                                                ErrorMessages.PHONE_CONFIRM)

    def __base_init(self) -> None:
        self.selenium_base.driver.get(Main.AUTH_PAGE)
        self.__check_add_account_button()
        self.__select_email_type()

    def __select_email_type(self) -> None:
        login_type_button = self.selenium_base.find_elements(By.CSS_SELECTOR,
                                                             Selectors.LOGIN_TYPE_SELECTOR)[0]
        login_type_button.click()

    def __check_add_account_button(self) -> None:
        add_account_button = self.selenium_base.find_element(By.CLASS_NAME, Selectors.ADD_ACCOUNT_BUTTON_CLASS)
        if add_account_button:
            add_account_button.click()

    def __wait_for_element_disappeared(self, selector: str, by: By, error_message: ErrorMessages, timeout=30) -> None:
        counter = 0
        element = self.selenium_base.find_element(by, selector)
        if element:
            while counter < timeout:
                element = self.selenium_base.find_element(by, selector)
                counter += 1
                if not element:
                    break
                time.sleep(1)
            assert not element, error_message

    @staticmethod
    def __fill_input(element: WebElement, value: str) -> None:
        element.send_keys(value, Keys.ENTER)
