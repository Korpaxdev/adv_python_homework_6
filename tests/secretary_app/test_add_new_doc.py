import pytest
from random import randrange
from secretary_app.app import add_new_doc, documents, directories
from itertools import chain


def generate_random_passport_number():
    """Генерирует рандомный паспортный номер"""
    return f"{randrange(0000, 5550)} {randrange(000000, 999999)}"


def generate_random_shelf_number():
    """Генерирует рандомный номер полки"""
    return str(randrange(1, 100))


def generate_document_list(doc_count=5):
    """
    Создает список из документов, с рандомными данными.
    :params
        - doc_count - количество документов, которые необходимо создать (default = 5)
    """
    new_documents = []
    for i in range(1, doc_count + 1):
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
    """
    Тест по добавлению нового документа в базу (add_new_doc)
    assert - Проверяется, что документ с номером существует в documents и directories
    """
    props = iter([doc_number, doc_type, doc_owner, doc_shelf])
    monkeypatch.setattr('builtins.input', lambda _: next(props))
    value = add_new_doc()
    assert any(doc_number in d.values() for d in documents) and doc_number in chain(*directories.values())
    print(f"\n{documents=}")
    print(f"{directories=}")
