from secretary_app.app import show_all_docs_info, documents, directories


def test_show_all_docs_info():
    print()
    result = show_all_docs_info()
    assert result
    print(f'{documents=}')
    print(f'{directories=}')
