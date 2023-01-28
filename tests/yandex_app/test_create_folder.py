import pytest
from tests.yandex_app.enums.yandex_enums import YandexEnum


@pytest.mark.parametrize('folder_name', YandexEnum.FOLDER_NAMES.value)
def test_create_folder(yandex_api, folder_name):
    yandex_api \
        .assert_authorized() \
        .create_folder(folder_name)
