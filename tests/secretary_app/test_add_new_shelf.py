import pytest
from secretary_app.app import add_new_shelf, directories
from random import randrange


@pytest.mark.parametrize('shelf_number', ['1', '2', '3', '4', 'None', None, ''])
def test_add_new_shelf(monkeypatch, shelf_number):
    """
    Тест на добавление новой полки в directories (add_new_shelf)
    assert - Проверка на существование result_shelf_number в directories
    """
    monkeypatch.setattr('builtins.input', lambda _: str(randrange(1, 100)))
    result_shelf_number, result = add_new_shelf(shelf_number)
    assert result_shelf_number in directories
    print(f"\n{result_shelf_number=}")
    print(f"\n{directories=}")
