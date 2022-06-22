from base_page import Base_Page
from LOCATORS import Locators

class Main_Page(Base_Page):
    '''В данном классе описаны основные действия, осуществляемые на главной странице'''

    def check_image_link(self):
        '''Проверяет существование ссылки "Картинки"'''
        return self.find_element(Locators.LOCATOR_IMAGE_LINK)

    def check_url_after_image_link_click(self):
        '''Возвращает url браузера, после клика по ссылке "Картинки" '''
        self.check_image_link().click()
        url = self.get_activ_url()
        return url

class Image_Page(Base_Page):
    '''В данном классе описаны основные действия, осуществляемые на странице
    с картинками'''

    def __return_first_cat_link(self):
        '''Возвращает ссылку первой категории с картинками'''
        return self.find_element(Locators.LOCATOR_FIRST_CAT_LINK)

    def __return_search_field_after_click(self):
        '''Возвращает поле поиска'''
        return self.find_element(Locators.LOCATOR_SEARCH_FIELD)

    def __return_first_small_image_link(self):
        '''Возвращает первую ссылку на картинку'''
        return self.find_element(Locators.LOCATOR_SMALL_FIRST_LINK)

    def __return_open_image_after_click(self):
        '''Возвращает открытую картинку (после нажатия)'''
        return self.find_element(Locators.LOCATOR_OPEN_IMAGE)

    def check_text_cat_in_search_field(self):
        '''Функция для проверки того, что название категории
        вводится в поле поиска, после нажатия на категорию.
        Возвращает True, если это так.'''
        first_link = self.__return_first_cat_link()
        first_link_text = first_link.get_attribute('innerText')
        first_link.click()
        search_field_after_click = self.__return_search_field_after_click()
        if first_link_text==search_field_after_click.get_attribute('value'):
            return True
        else:
            return False

    def open_first_cat_link(self):
        '''Функция открывает первую категорию картинок'''
        first_cat_link = self.__return_first_cat_link()
        first_cat_link.click()

    def open_first_image(self):
        '''Функция открывает первую картинку'''
        self.find_element(Locators.LOCATOR_SMALL_FIRST_LINK).click()

    def click_forward_button(self):
        '''Функция иммитирует клик на кнопку впереёд в слайдере яндекса'''
        self.find_element(Locators.LOCATOR_BUTTON_FORWARD).click()

    def click_backward_button(self):
        '''Функция иммитирует клик на кнопку впереёд в слайдере яндекса'''
        self.find_element(Locators.LOCATOR_BUTTON_BACKWARD).click()

    def return_open_image_src(self):
        '''Возвращает аттрибут src открытой картинки (первой в слайдере,
        самой большой)'''
        open_img = self.__return_open_image_after_click()
        return open_img.get_attribute('src')
    '''
    def check_open_image_after_click(self):
        small_link = self.__return_first_small_image_link()
        small_link.click()
        src_img = self.__return_open_image_after_click().get_attribute('src')
        if src_img == small_link.get_attribute('href'):
            return True '''




