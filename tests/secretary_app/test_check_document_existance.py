import pytest
from secretary_app.app import check_document_existance


@pytest.mark.parametrize('document_number', [
    1, "11-2", "10006", 'a', 1.5, None, ""
])
def test_check_document_existence(document_number):
    """
    Тест на существование документа в documents (check_document_existence)
    assert - Результат работы должен быть типа bool
    """
    doc_founded = check_document_existance(document_number)
    assert isinstance(doc_founded, bool)
    print(f"\n{doc_founded=}")
