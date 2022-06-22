from selenium.webdriver.common.by import By

class Locators:
    '''В данном классе описаны все локаторы для поиска элементов'''
    LOCATOR_IMAGE_LINK = (By.LINK_TEXT, 'Картинки')
    LOCATOR_FIRST_CAT_LINK = (By.XPATH, '//div[@class="PopularRequestList"]/div[1]/a')
    LOCATOR_SEARCH_FIELD = (By.XPATH, '/html/body/header/div/div[1]/div[2]/form/div[1]/span/span/input')
    LOCATOR_FIRST_IMG_LINK = (By.XPATH, '//a[@class="serp-item__link"][1]')
    LOCATOR_SMALL_FIRST_IMG = (By.XPATH, '//div[3]/div[2]/div[1]/div[1]/div/div[1]/div/a/img')
    LOCATOR_OPEN_IMAGE = (By.XPATH, '//div[12]/div[2]/div/div/div/div[3]/div/div[2]/div[1]/div[3]/div/img')
    LOCATOR_BUTTON_FORWARD = (By.XPATH, '//div[12]/div[2]/div/div/div/div[3]/div/div[2]/div[1]/div[4]/i')
    LOCATOR_BUTTON_BACKWARD = (By.XPATH, '//div[12]/div[2]/div/div/div/div[3]/div/div[2]/div[1]/div[1]/i')
    LOCATOR_SMALL_FIRST_LINK = (By.XPATH,'//div[3]/div[2]/div[1]/div[1]/div/div[1]/div/a')