from dataclasses import dataclass


@dataclass(frozen=True)
class Main:
    BASE_URL = 'https://cloud-api.yandex.net/v1/disk'
    RESOURCE_URL = f'{BASE_URL}/resources'
    TOKEN = ''  # Вставьте ваш токен авторизации сюда
    FOLDER_NAMES = [None, False, True, 123, 'Tests', 'None', 'False', 'True', '1.25', 'Tests/Something',
                    'Another_test/Something', '']  # Имена папок для test_create_folder


@dataclass(frozen=True)
class StatusCodes:
    CODE_201 = 201
    CODE_200 = 200
    OK_STATUS_CODES = [CODE_201, CODE_200]


@dataclass(frozen=True)
class Errors:
    # Шаблон строки ответа в случае False в assert
    WRONG_STATUS_CODE_FORMAT = '\n[STATUS CODE]: {status_code}\n[MESSAGE]: {text}'
