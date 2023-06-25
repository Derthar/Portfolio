from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def __init__(self, browser, link):
        self.link = link
        self.item_name = ''
        self.item_price = ''
        super().__init__(browser, self.link)

    def should_be_succes_message(self):
        assert self.is_present(*ProductPageLocators.SUCCESS_MESSAGE), 'Succes message is present'

    def should_not_be_succes_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), 'Succes message is present'

    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN).click()

    def get_data_about_product(self):
        self.item_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        self.item_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def __get_data_about_product_from_message(self):
        self.actual_product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_FROM_MESSAGE).text
        self.actual_product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_FROM_MESSAGE).text

    def compare_data_about_product(self):
        self.__get_data_about_product_from_message()
        assert self.item_name == self.actual_product_name, 'Имена товаров не совпадают'
        assert self.item_price == self.actual_product_price, 'Стоимости товаров не совпадают'
