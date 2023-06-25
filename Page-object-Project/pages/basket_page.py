from selenium.common import NoSuchElementException
from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def __init__(self, browser, link):
        self.link = link
        super().__init__(browser, link)

    def should_be_basket_page(self):
        self.__should_be_basket_url()
        self.__should_be_basket_form()

    def __should_be_basket_url(self):
        assert 'basket' in self.browser.current_url

    def __should_be_basket_form(self):
        try:
            header = self.browser.find_element(*BasketPageLocators.BASKET_HEADER).text
            assert 'Basket' == header, 'Its not basket page'
        except NoSuchElementException:
            'Basket header element not found'

    def should_be_empty_basket_text(self):
        try:
            empty_text = self.browser.find_element(*BasketPageLocators.BASKET_EMPTY_TEXT).text
            assert 'empty' in empty_text, 'Basket is not empty'
        except NoSuchElementException:
            'Basket empty text is not found'

    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), 'Basket is not empty'
