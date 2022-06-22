from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Base_Page:
    '''Данный класс описывает работу веб-драйвера.
    Является родительским для всех классов-объектов страниц'''

    def __init__(self, driver, url):
        '''Инициализатор, опеределяет драйвер, url, сразу переходит по нужному url'у'''
        self.driver = driver
        self.url = url
        self.go_to_website()

    def go_to_website(self):
        '''Функция открытия веб-страницы, url которой ожидает инициализатор'''
        return self.driver.get(self.url)

    def find_element(self, locator, time=5):
        '''Функция возвращает элемент веб-страницы по её локатору'''
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(\
            locator), message='Не удаётся найти элемент по локатору.')

    def get_link(self, link):
        '''Функция принимает на вход html-ссылку, возвразает её url'''
        return link.get_attribute('href')

    def word_text(self, element, text):
        '''Функция заполняет element веб-страницы текстом text'''
        element.send_keys(text)
