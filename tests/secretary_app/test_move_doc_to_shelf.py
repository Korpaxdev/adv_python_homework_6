import pytest
from random import randrange
from secretary_app.app import move_doc_to_shelf, directories


@pytest.mark.parametrize('doc_number, shelf_number', [
    ('11-2', str(randrange(3, 100))),
    ('2207 876234', str(randrange(3, 100))),
    ('None', '3'),
    ('Something', str(randrange(3, 100))),
    ('5455 028765', str(randrange(3, 100)))

])
def test_move_doc_to_shelf(doc_number, shelf_number, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda x: doc_number if x == 'Введите номер документа - ' else shelf_number)
    result = move_doc_to_shelf()
    assert isinstance(result, bool)
    if result:
        assert doc_number in directories[shelf_number]
    print(f"\n{directories=}")
