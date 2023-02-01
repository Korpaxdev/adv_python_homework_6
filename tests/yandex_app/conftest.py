import pytest
from tests.yandex_app.classes.yandex_class import YandexAPI
from tests.yandex_app.utils.constants import Main


@pytest.fixture(scope='session')
def yandex_api():
    return YandexAPI(Main.TOKEN)
