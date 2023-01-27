from secretary_app.app import get_all_doc_owners_names


def test_get_all_doc_owners_names():
    docs = get_all_doc_owners_names()
    assert isinstance(docs, set | None)
    print(f"\n{docs=}")
