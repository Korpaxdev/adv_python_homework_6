import pytest
from secretary_app.app import append_doc_to_shelf, directories
from random import randrange


@pytest.mark.parametrize('doc_number, shelf_number', [
    ('11-2', '3'),
    ('10006', '3'),
    ('128', '5'),
    ('6000', str(randrange(1, 1000)))
])
def test_append_doc_to_shelf(doc_number, shelf_number):
    """
    Тест на добавление номера документа в directories (append_doc_to_shelf)
    assert - Проверка существования doc_number в directories
    """
    append_doc_to_shelf(doc_number, shelf_number)
    assert doc_number in directories[shelf_number]
    print(f"\n{directories=}")
