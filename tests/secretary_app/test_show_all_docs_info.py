from secretary_app.app import show_all_docs_info, documents, directories


def test_show_all_docs_info():
    """
    Тест на печать всех документов (show_all_docs_info)
    assert - Результат должен быть True
    """
    print()
    result = show_all_docs_info()
    assert result
    print(f'{documents=}')
    print(f'{directories=}')
