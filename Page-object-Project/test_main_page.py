import time
import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage


main_link = "http://selenium1py.pythonanywhere.com/"


@pytest.mark.login_guest
@pytest.mark.new
class TestLoginFromMainPage:
    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser, main_link)
        page.open()

        # Инициализация новой страницы в теле теста (Return в функции-переходе отключен)
        page.go_to_login_page()  # Переход по ссылке

        # Присваивание получившейся странице нового имени и класса (с сохранением текущего урл)
        login_page = LoginPage(browser=browser, link=browser.current_url)
        login_page.should_be_login_page()
        time.sleep(10)


    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, main_link)
        page.open()
        page.should_be_login_link()
        time.sleep(10)


def  test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = MainPage(browser, main_link)
    page.open()
    page.go_to_basket_page()
    page = BasketPage(browser, link=browser.current_url)
    page.should_be_basket_page()
    page.should_be_empty_basket()
    page.should_be_empty_basket_text()


