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
        """
        Валидация поля ввода email
        1. Если нет такого поля будет ошибка EMAIL_INPUT_NOT_FOUND
        2. Если в ходе ввода появился элемент login_hint, то тоже будет ошибка с содержимым элемента
        """
        email_input = self.selenium_base.find_element(By.CSS_SELECTOR, Selectors.EMAIL_INPUT_ID, timeout=2)
        assert email_input, ErrorMessages.EMAIL_INPUT_NOT_FOUND
        self.__fill_input(email_input, self.login)
        login_hint = self.selenium_base.find_element(By.CSS_SELECTOR, Selectors.EMAIL_HINT_ID)
        assert not login_hint, ErrorMessages.FORMAT_MESSAGE.format(text=login_hint.text)
        return self

    def validate_password(self) -> None:
        """
        Валидация пароля. Должна использоваться, только в случае успешной валидации email
        1. Если поля для ввода пароля нет, то происходит проверка, на то что появилось ли поля входа по QR CODE
        2. Если поле есть, но так же появилось поле для ввода CAPTCHA, то будет ошибка PASSWORD_CAPTCHA
        3. Если после ввода пароля, появился элемент password_hint, то будет ошибка с содержимым этого элемента
        4. После успешного ввода пароля, происходит проверка на подтверждение номера телефона
        """
        password_input = self.selenium_base.find_element(By.CSS_SELECTOR, Selectors.PASSWORD_INPUT_ID)
        if not password_input:
            return self.__check_qr_code()
        self.__fill_input(password_input, self.password)
        password_captcha = self.selenium_base.find_element(By.CSS_SELECTOR, Selectors.PASSWORD_CAPTCHA_CLASS)
        assert not password_captcha, ErrorMessages.PASSWORD_CAPTCHA
        password_hint = self.selenium_base.find_element(By.CSS_SELECTOR, Selectors.PASSWORD_HINT_ID)
        assert not password_hint, ErrorMessages.FORMAT_MESSAGE.format(text=password_hint.text)
        self.__check_phone_number()

    def __check_qr_code(self) -> None:
        """
        1. Проверка на появление QR_CODE
        2. Если элемент есть, будет дано 30 сек (по умолчанию),
        на то чтобы его подтвердить (чтобы элемент исчез на странице),
        если элемент не исчез, то будет вызвана ошибка QR_CODE
        """
        self.__wait_for_element_disappeared(Selectors.QR_CODE_CLASS, By.CSS_SELECTOR, ErrorMessages.QR_CODE)

    def __check_phone_number(self) -> None:
        """
        1. Проверяет - появилась ли кнопка подтверждения номера телефона.
        2. В случае появление кнопки, драйвер жмет на нее
        3. Дальше в течении 30 сек (по умолчанию) ожидает, когда исчезнет со страницы поле для ввода кода.
        (Поле для ввода исчезнет, если ввести верный код с телефона)
        4. Если поле не исчезает, то будет ошибка PHONE_CONFIRM
        """
        phone_confirm_button = self.selenium_base.find_element(By.CSS_SELECTOR, Selectors.PHONE_CONFIRM_BUTTON_SELECTOR)
        if phone_confirm_button:
            phone_confirm_button.click()
            self.__wait_for_element_disappeared(Selectors.PHONE_CODE_FIELD_CLASS, By.CSS_SELECTOR,
                                                ErrorMessages.PHONE_CONFIRM)

    def __base_init(self) -> None:
        """
        Базовая инициализация.
        1. Драйвер переходит на страницу входа
        2. Проверяет если на странице входа есть кнопка добавить аккаунт, то нажимает на нее
        3. Выбирает тип входа по email
        """
        self.selenium_base.driver.get(Main.AUTH_PAGE)
        self.__check_add_account_button()
        self.__select_email_type()

    def __select_email_type(self) -> None:
        """
        Выбирает тип авторизации по email и password
        """
        login_type_button = self.selenium_base.find_elements(By.CSS_SELECTOR,
                                                             Selectors.LOGIN_TYPE_SELECTOR)[0]
        if login_type_button:
            login_type_button.click()

    def __check_add_account_button(self) -> None:
        """
        Нажимает на кнопку добавить аккаунт, если такая кнопка есть на странице
        """
        add_account_button = self.selenium_base.find_element(By.CSS_SELECTOR, Selectors.ADD_ACCOUNT_BUTTON_CLASS)
        if add_account_button:
            add_account_button.click()

    def __wait_for_element_disappeared(self, selector: str, by: By, error_message: ErrorMessages, timeout=30) -> None:
        """
        Ожидает в течении timeout, когда элемент по selector исчезнет со страницы.
        Если такого не произошло, то вызывает ошибку error_message
        :params
        - selector - строка с селектором элемента. Предпочтительно использовать класс SELECTORS
        - by - класс By из webdriver. Определяет, как искать данный элемент
        - error_message - класс ErrorMessages. Ошибка в случае, когда истечет timeout
        - timeout - int. Количество секунд, в течении которых будет происходить проверка на отсутствие элемента.
        По умолчанию (30 сек)
        """
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
        """
        Заполняет element значением из value и жмет ENTER
        :params
        - element - WebElement со страницы
        - value - строка с значением
        """
        element.send_keys(value, Keys.ENTER)
