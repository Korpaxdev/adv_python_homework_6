import pytest
from itertools import chain
from secretary_app.app import remove_doc_from_shelf, directories


@pytest.mark.parametrize('doc_number', ['11-2', '10006', "10", None, ""])
def test_remove_doc_from_shelf(doc_number):
    """
    Тест на удаление документа с полки (remove_doc_from_shelf)
    asset - doc_number не должен существовать в directories
    """
    remove_doc_from_shelf(doc_number)
    assert doc_number not in chain(*directories.values())
    print(f"{directories=}")
