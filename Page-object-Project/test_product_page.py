import time
import pytest
from pages.locators import MainPageLocators
from pages.locators import ProductPageLocators
from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
from faker import Faker


main_link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
login_link = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser=browser, link=main_link)
    page.open()
    page.should_not_be_succes_message()
    page.get_data_about_product()
    page.add_to_basket()
    page.is_appeared(*ProductPageLocators.SUCCESS_MESSAGE)
    page.compare_data_about_product()
    time.sleep(1)


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, main_link)
    page.open()
    page.browser.find_element(*MainPageLocators.ADD_TO_BASKET).click()
    assert page.is_not_element_present(*MainPageLocators.SUCCESS_MESSAGE)


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, main_link)
    page.open()
    assert page.is_not_element_present(*MainPageLocators.SUCCESS_MESSAGE)


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, main_link)
    page.open()
    page.browser.find_element(*MainPageLocators.ADD_TO_BASKET).click()
    assert page.is_disappeared(*MainPageLocators.SUCCESS_MESSAGE)


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, main_link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, main_link)
    page.open()
    page.go_to_login_page()
    page = LoginPage(browser, link=browser.current_url)
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, main_link)
    page.open()
    page.go_to_basket_page()
    page = BasketPage(browser, link=browser.current_url)
    page.should_be_basket_page()
    page.should_be_empty_basket()
    page.should_be_empty_basket_text()


@pytest.mark.user
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        page = LoginPage(browser, login_link)
        page.open()
        page.register_new_user(Faker().email(), Faker().password())
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, main_link)
        page.open()
        assert page.is_not_element_present(*MainPageLocators.SUCCESS_MESSAGE)

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser=browser, link=main_link)
        page.open()
        page.should_not_be_succes_message()
        page.get_data_about_product()
        page.add_to_basket()
        page.is_appeared(*ProductPageLocators.SUCCESS_MESSAGE)
        page.compare_data_about_product()
