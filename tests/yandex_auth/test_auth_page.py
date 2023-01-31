import pytest

from tests.yandex_auth.classes.auth_page import AuthPage
from tests.yandex_auth.utils.constatnts import AuthData


@pytest.mark.parametrize('login, password', AuthData.TESTS_DATA)
def test_auth_page(get_selenium_base, login, password):
    auth_page = AuthPage(get_selenium_base, login, password)
    auth_page.validate_email().validate_password()
    print(f'[SUCCESS]: Вход с {login=} {password=} успешен')
