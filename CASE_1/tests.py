from page_objects import Main_Page, Search_Result_Page
from config import *

def test_exist_search_field(browser):
    '''Тест на существование поля поиска на главной странице'''
    main_page = Main_Page(browser, MAIN_PAGE_URL)
    flag = main_page.return_search_field()
    assert flag

def test_exist_aux_table(browser):
    '''Тест на появление таблицы с подсказками после заполнения поля поиска'''
    main_page = Main_Page(browser, MAIN_PAGE_URL)
    main_page.word_text_in_search_field('Тензор')
    flag = main_page.is_auxiliary_table_exist()
    assert flag

def test_first_url_link(browser):
    '''Функция проверки url'a первой ссылки страницы результатов'''
    search_result_page = Search_Result_Page(browser, SEARCH_RESULT_PAGE_URL)
    first_url = search_result_page.first_search_table_link()
    assert first_url == expected_url