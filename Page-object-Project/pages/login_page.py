from .base_page import BasePage
from .locators import LoginPageLocators


# Класс страницы логина/регистрации
class LoginPage(BasePage):
    def __init__(self, browser, link):
        self.link = link
        super().__init__(browser, self.link)

    # Проверка, что это страница логина
    def should_be_login_page(self):
        self.__should_be_login_url()
        self.__should_be_login_form()
        self.__should_be_register_form()
        return True

    # Проверка ссылки
    def __should_be_login_url(self):
        assert 'login' in self.browser.current_url, 'This is not login url'

    # Проверка наличия формы логина
    def __should_be_login_form(self):
        assert self.browser.find_element(*LoginPageLocators.LOGIN_FORM), 'There is no login form'

    # Проверка наличия формы регистрации
    def __should_be_register_form(self):
        assert self.browser.find_element(*LoginPageLocators.REGISTER_FORM), 'There is no register form'

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.REGISTER_FORM_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTER_FORM_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_FORM_CONFIRM_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_FORM_SUBMIT_BUTTON).click()
