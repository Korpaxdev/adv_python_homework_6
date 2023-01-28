import pytest
from secretary_app.app import get_doc_owner_name


@pytest.mark.parametrize('doc_number', ['10006', "11-2", '5455 028765', '2207 876234', 12, None, ""])
def test_get_owner_name(monkeypatch, doc_number):
    """
    Тест на получение имени владельца по номеру документа (get_owner_name)
    assert - Результат работы должен быть типом str или None
    """
    monkeypatch.setattr('builtins.input', lambda _: doc_number)
    doc = get_doc_owner_name()
    assert isinstance(doc, str | None)
    print(f"{doc=}")
