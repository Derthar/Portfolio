import pytest
from selenium import webdriver


# Добавление параметров запуска тестов
def pytest_addoption(parser):

    # Параметр выбора браузера
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")

    # Параметр выбора языка запуска
    parser.addoption('--language', action='store', default=None,
                     help="Choose the language: ru, en, fr, ...")


@pytest.fixture(scope="function")
def browser(request):

    # Получение параметров из команды запуска теста
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")

    # Выбор браузера
    if browser_name == "chrome":
        from selenium.webdriver.chrome.options import Options
        print("\nstart chrome browser for test...")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})  # Установка языка
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        from selenium.webdriver.firefox.options import Options
        print("\nstart firefox browser for test..")
        options = Options()
        options.set_preference("intl.accept_languages", user_language)  # Установка языка
        browser = webdriver.Firefox(options=options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
