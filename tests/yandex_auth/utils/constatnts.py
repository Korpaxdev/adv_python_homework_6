from dataclasses import dataclass


@dataclass(frozen=True)
class Main:
    AUTH_PAGE = 'https://passport.yandex.ru/auth'


@dataclass(frozen=True)
class Selectors:
    EMAIL_INPUT_ID = '#passp-field-login'
    EMAIL_HINT_ID = '#field\:input-login\:hint'
    PASSWORD_INPUT_ID = '#passp-field-passwd'
    PASSWORD_HINT_ID = '#field\:input-passwd\:hint'
    QR_CODE_CLASS = '.MagicField-qr'
    PASSWORD_CAPTCHA_CLASS = '.AuthPasswordForm-captcha'
    LOGIN_TYPE_SELECTOR = '.AuthLoginInputToggle-type > button'
    PHONE_CONFIRM_BUTTON_SELECTOR = '[data-t=challenge_sumbit_phone-confirmation] > button'
    PHONE_CODE_FIELD_CLASS = '.CodeField'
    ADD_ACCOUNT_BUTTON_CLASS = '.AddAccountButton'


@dataclass(frozen=True)
class ErrorMessages:
    EMAIL_INPUT_NOT_FOUND = '[ERROR]: Input для ввода почты не найден'
    QR_CODE = '[ERROR]: Для входа необходимо использовать QR CODE'
    PASSWORD_CAPTCHA = '[ERROR]: Предпринято много попыток для входа. Необходимо ввести captcha'
    PHONE_CONFIRM = '[ERROR]: Необходимо подтверждение номера телефона'
    FORMAT_MESSAGE = '[ERROR]: {text}'


TEST_DATA = [
    # Тестовые данные для тестирования в test_auth_page.
    # В эти данные можете добавить свой аккаунт, для проверки входа
    # Шаблон - (email, password)
    ('', ''),
    (1, '123'),
    ('HELLO', 123),
    ('qweraiwdzxc', 'None'),
]
