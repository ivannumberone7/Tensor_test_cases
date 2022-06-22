from page_objects import Main_Page, Image_Page
from config import *

def test_exist_image_link(browser):
    '''Тест проверяющий существование ссылки "Картинки" на главной
    странице'''
    main_page = Main_Page(browser, MAIN_PAGE_URL)
    main_page.go_to_website()
    flag = main_page.check_image_link()
    assert flag

def test_check_expected_url_after_click(browser):
    '''Тест проверяющий URL браузера после клика на ссылку
    "Картинки"'''
    main_page = Main_Page(browser, MAIN_PAGE_URL)
    main_page.go_to_website()
    url = main_page.check_url_after_image_link_click()
    assert url == IMAGE_PAGE_URL

def test_cat_link_text_in_search_field_after_click(browser):
    '''Тест, проверяющий остаётся ли название категории в поле поиска,
    после клика на эту категорию'''
    image_page = Image_Page(browser, IMAGE_PAGE_URL)
    image_page.go_to_website()
    flag = image_page.check_text_cat_in_search_field()
    assert flag

def test_change_image_after_click_forward_button(browser):
    '''Тест для проверки того, что при нажатии на клавишу "вперёд"
    (в режиме слайдера) картинка меняется'''
    image_page = Image_Page(browser, IMAGE_PAGE_URL)
    image_page.go_to_website()
    image_page.open_first_cat_link()
    image_page.open_first_image()
    src1 = image_page.return_open_image_src()
    image_page.click_forward_button()
    src2 = image_page.return_open_image_src()
    assert src1!=src2

def test_no_changed_image_after_two_clicks(browser):
    '''Тест для проверки того, что при нажатии на клавишу "вперёд"
       (в режиме слайдера), а потом клавиши "назад"
        картинка остаётся прежней'''
    image_page = Image_Page(browser, IMAGE_PAGE_URL)
    image_page.go_to_website()
    image_page.open_first_cat_link()
    image_page.open_first_image()
    src1 = image_page.return_open_image_src()
    image_page.click_forward_button()
    image_page.click_backward_button()
    src2 = image_page.return_open_image_src()
    assert src1 == src2

