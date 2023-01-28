import requests
from tests.yandex_app.enums.yandex_enums import YandexEnum, StatusCodesEnum, ErrorsEnum
from typing import TypeVar

Self = TypeVar('Self', bound='YandexAPI')


class YandexAPI:

    def __init__(self, auth_token: str):
        self._header = {'Authorization': auth_token}

    def assert_authorized(self) -> Self:
        """
        Проверка авторизации
        assert - Статус код должен быть 200
        """
        response = requests.get(YandexEnum.BASE_URL.value, headers=self._header)
        assert response.status_code == StatusCodesEnum.CODE_200.value, self.get_error_string(response)
        return self

    def create_folder(self, folder_name: str = 'Test') -> Self:
        """
        Пытается создать папку с folder_path
        assert - Успешный ответ от сервера (status code - 200 or 201)
        """
        params = {'path': folder_name}
        response = requests.put(url=YandexEnum.RESOURCE_URL.value, params=params, headers=self._header)
        self.validate_status_code(response)
        return self

    def validate_status_code(self, response: requests.Response):
        assert response.status_code in StatusCodesEnum.OK_STATUS_CODES.value, self.get_error_string(response)

    @staticmethod
    def get_error_string(response: requests.Response) -> str:
        status_code = response.status_code
        text = response.text
        return ErrorsEnum.WRONG_STATUS_CODE_FORMAT.value.format(status_code=status_code, text=text)
