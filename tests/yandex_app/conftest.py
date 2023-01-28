import pytest
from tests.yandex_app.classes.yandex_class import YandexAPI
from tests.yandex_app.enums.yandex_enums import YandexEnum


@pytest.fixture(scope='session')
def yandex_api():
    return YandexAPI(YandexEnum.TOKEN.value)
