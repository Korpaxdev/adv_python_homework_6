import pytest

from tests.yandex_auth.classes.auth_page import AuthPage
from tests.yandex_auth.utils.constatnts import TEST_DATA


@pytest.mark.parametrize('login, password', TEST_DATA)
def test_auth_page(get_selenium_base, login, password):
    """
    Тестирование страницы входа Main.AUTH_PAGE.
    Для правильного тестирования, можете добавить свои данные в TEST_DATA
    Тестирование проводится только в режиме ввода почты и пароля
    В случае если появится QR CODE или подтверждение по телефону,
    будет дано 30 сек (по умолчанию) на то, чтобы подтвердить QR_CODe или номер телефона
    """
    auth_page = AuthPage(get_selenium_base, login, password)
    auth_page.validate_email().validate_password()
    print(f'[SUCCESS]: Вход с {login=} {password=} успешен')
