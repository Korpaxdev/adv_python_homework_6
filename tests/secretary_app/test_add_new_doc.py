import pytest
from random import randrange
from secretary_app.app import add_new_doc, documents, directories
from itertools import chain


def doc_input_gen(props):
    for prop in props:
        yield prop


def generate_random_passport_number():
    return f"{randrange(0000, 5550)} {randrange(000000, 999999)}"


def generate_random_shelf_number():
    return str(randrange(1, 100))


def generate_document_list(count=5):
    new_documents = []
    for i in range(1, count + 1):
        doc_number = generate_random_passport_number()
        doc_type = 'passport'
        doc_owner = f'Something{i}'
        doc_shelf = generate_random_shelf_number()
        new_documents.append((doc_number, doc_type, doc_owner, doc_shelf))
    return new_documents


@pytest.mark.parametrize('doc_number, doc_type, doc_owner, doc_shelf', [
    *generate_document_list(),
    ('11-2', 'invoice', 'Гена', '5')
])
def test_add_new_doc(monkeypatch, doc_number, doc_type, doc_owner, doc_shelf):
    props = iter([doc_number, doc_type, doc_owner, doc_shelf])
    monkeypatch.setattr('builtins.input', lambda _: next(props))
    value = add_new_doc()
    assert any(doc_number in d.values() for d in documents) and doc_number in chain(*directories.values())
    print(f"\n{documents=}")
    print(f"{directories=}")
