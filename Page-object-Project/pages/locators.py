from selenium.webdriver.common.by import By


# Локаторы базовой страницы
class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inv")
    BASKET_LINK = (By.CSS_SELECTOR, 'div.basket-mini a.btn.btn-default')
    BASKET_EMPTY_MESSAGE = (By.CSS_SELECTOR, 'div#content_inner p')
    USER_ICON = (By.CSS_SELECTOR, '.icon-user')


# Локаторы главной страницы
class MainPageLocators:
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, 'div.alert')
    ADD_TO_BASKET = (By.CSS_SELECTOR, 'button.btn-add-to-basket')


class ProductPageLocators:
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, 'div.alert')
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main p')
    PRODUCT_NAME_FROM_MESSAGE = (By.CSS_SELECTOR, '.alertinner strong')
    PRODUCT_PRICE_FROM_MESSAGE = (By.CSS_SELECTOR, '.alertinner p strong')


# Локаторы страницы регистрации
class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '.login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '.register_form')
    REGISTER_FORM_EMAIL = (By.CSS_SELECTOR, 'input.form-control[name=registration-email]')
    REGISTER_FORM_PASSWORD = (By.CSS_SELECTOR, 'input.form-control[name=registration-password1]')
    REGISTER_FORM_CONFIRM_PASSWORD = (By.CSS_SELECTOR, 'input.form-control[name=registration-password2]')
    REGISTER_FORM_SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[name=registration_submit]')


# Локаторы страницы корзины
class BasketPageLocators:
    BASKET_HEADER = (By.CSS_SELECTOR, 'div h1')
    BASKET_EMPTY_TEXT = (By.CSS_SELECTOR, '#content_inner p')
    BASKET_ITEMS = (By.CSS_SELECTOR, '.basket-items')
