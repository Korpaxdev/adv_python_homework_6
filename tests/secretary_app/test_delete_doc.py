import pytest
from secretary_app.app import delete_doc, documents, directories
from random import randrange
from itertools import chain


@pytest.mark.parametrize('doc_number', ['11-2', '10006', str(randrange(1000, 2000)), None, ""])
def test_delete_doc(doc_number, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: doc_number)
    delete_doc()
    assert not any(doc_number in d.values() for d in documents) and doc_number not in chain(*directories.values())
    print(f"\n{documents=}")
    print(f"{directories=}")
