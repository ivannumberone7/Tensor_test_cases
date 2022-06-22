from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Base_Page:
    '''Данный класс описывает работу веб-драйвера.
    Является родительским для всех классов-объектов страниц'''

    def __init__(self, driver, url):
        '''Инициализатор, опеределяет драйвер, url'''
        self.driver = driver
        self.url = url

    def find_element(self, locator, time=5):
        '''Функция возвращает элемент веб-страницы по её локатору'''
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(\
            locator), message='Не удаётся найти элемент по локатору.')

    def go_to_website(self):
        '''Функция открытия веб-страницы, url которой ожидает инициализатор'''
        return self.driver.get(self.url)

    def get_activ_url(self, slice=True):
        '''Возвращает активный url окна, если slice = True, форматирует его'''
        self.driver.switch_to.window(self.driver.window_handles[-1])
        url = self.driver.current_url
        if slice:
            url = url[0:url.rfind('/') + 1]
        return url
