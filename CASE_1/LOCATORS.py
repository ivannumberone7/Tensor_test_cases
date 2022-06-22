from selenium.webdriver.common.by import By

class Locators:
    '''В данном классе описаны все локаторы для поиска необходимых элементов'''
    LOCATOR_SEARCH_FIELD = (By.ID, 'text')
    LOCATOR_AUXILIARY_TABLE = (By.CLASS_NAME, 'mini-suggest__popup_visible')
    LOCATOR_FIRST_LINK_AFTER_SEARCH = (By.XPATH,'//*[@id="search-result"]/li[1]/div/div[1]/a')