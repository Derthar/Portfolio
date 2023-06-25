from selenium.common import NoSuchElementException, NoAlertPresentException, TimeoutException
import math
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from .locators import BasePageLocators


# Базовый класс страницы
class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    # Проверка наличия ссылки логина
    def should_be_login_link(self):
        assert self.browser.find_element(*BasePageLocators.LOGIN_LINK), "Login link is not presented!"
        # * нужна для распаковки кортежа

    # Переход на страницу логина
    def go_to_login_page(self):
        self.browser.find_element(*BasePageLocators.LOGIN_LINK).click()

    # Переход в корзину
    def go_to_basket_page(self):
        self.browser.find_element(*BasePageLocators.BASKET_LINK).click()

    # Проверка присутствия элемента на странице
    def is_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException as ex:
            print(ex)
            return False
        return True

    # Решение задачки и ввод ответа
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    # Элемент не должен присутствовать на странице
    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(ec.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    # Элемент должен исчезнуть со страницы в течении timeout
    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1).until_not(ec.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    # Элемент должен появиться со страницы в течении timeout
    def is_appeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1).until(ec.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def should_be_authorized_user(self):
        assert self.is_present(*BasePageLocators.USER_ICON), "User icon isn't presented,"\
                                                                             "probably unauthorised user"
