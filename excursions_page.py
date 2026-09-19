from selenium.webdriver.common.by import By


class ExcursionsPage:
    URL = "https://excursium.com/ekskursii-dlya-shkolnikov/list"

    def __init__(self, driver):
        self.driver = driver

    @property
    def page_title(self):
        return self.driver.title

    def open(self):
        self.driver.get(self.URL)
