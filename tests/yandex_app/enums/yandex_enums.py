from enum import Enum


class YandexEnum(Enum):
    BASE_URL = 'https://cloud-api.yandex.net/v1/disk'
    RESOURCE_URL = f'{BASE_URL}/resources'
    TOKEN = ''  # Вставьте ваш токен авторизации сюда
    FOLDER_NAMES = [None, False, True, 123, 'Tests', 'None', 'False', 'True', '1.25', 'Tests/Something',
                    'Another_test/Something', '']  # Имена папок для test_create_folder


class StatusCodesEnum(Enum):
    CODE_201 = 201
    CODE_200 = 200
    OK_STATUS_CODES = [CODE_201, CODE_200]


class ErrorsEnum(Enum):
    # Шаблон строки ответа в случае False в assert
    WRONG_STATUS_CODE_FORMAT = '\n[STATUS CODE]: {status_code}\n[MESSAGE]: {text}'
