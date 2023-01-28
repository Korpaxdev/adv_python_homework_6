import pytest
from random import randrange
from secretary_app.app import get_doc_shelf, directories


@pytest.mark.parametrize('doc_number', ['11-2', '10006', '2207 876234', 'None', None, str(randrange(1, 10000)), ""])
def test_get_doc_shelf(doc_number, monkeypatch):
    """
    Тест на получение номера полки документа по номеру документа (get_doc_shelf)
    assert - Результат работы должен быть типом None или str
    """
    monkeypatch.setattr('builtins.input', lambda _: doc_number)
    shelf_number = get_doc_shelf()
    assert isinstance(shelf_number, None | str)
    print(f"{shelf_number=}")
    print(f"{directories=}")
