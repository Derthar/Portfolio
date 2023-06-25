from .base_page import BasePage

link = 'http://selenium1py.pythonanywhere.com/'


# Класс главной страницы
class MainPage(BasePage):
    def __init__(self, browser, link):
        self.link = link
        super().__init__(browser, self.link)
