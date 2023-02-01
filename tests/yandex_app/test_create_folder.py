import pytest
from tests.yandex_app.utils.constants import Main


@pytest.mark.parametrize('folder_name', Main.FOLDER_NAMES)
def test_create_folder(yandex_api, folder_name):
    yandex_api \
        .assert_authorized() \
        .create_folder(folder_name)
