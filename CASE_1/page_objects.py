from base_page import Base_Page
from selenium. webdriver. common. keys import Keys
from LOCATORS import Locators

class Main_Page(Base_Page):
    '''В данном классе описаны основные действия, осуществляемые на главной странице'''

    def is_auxiliary_table_exist(self):
        '''Проверка на существовании таблицы с подсказками'''
        self.auxiliary_table = self.find_element(Locators.LOCATOR_AUXILIARY_TABLE)
        if self.auxiliary_table:
            return True

    def return_search_field(self):
        '''Возвращает поле поиска'''
        self.search_field = self.find_element(Locators.LOCATOR_SEARCH_FIELD)
        return self.search_field


    def word_text_in_search_field(self, text):
        '''Заполняет поле поиска текстом'''
        self.return_search_field()
        self.word_text(self.search_field, text)

    def press_enter_on_search_field(self):
        '''Нажатие на поле поиска клавиши ENTER'''
        self.search_field.send_keys(Keys.ENTER)

class Search_Result_Page(Base_Page):
    '''В данном классе описаны основные действия, осуществляемые на странице
    с результатми поиска'''

    def first_search_table_link(self):
        '''Получение ссылки 1 результата поиска'''
        first_link = self.find_element(Locators.LOCATOR_FIRST_LINK_AFTER_SEARCH)
        return self.get_link(first_link)







