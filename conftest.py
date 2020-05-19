import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose your language: ")


@pytest.fixture()
def browser(request):
    print("\nstart browser for test..")
    language = request.config.getoption("language")
    options = Options()
    # Реализуем английский интерфейс
    if language == "en":
        options.add_experimental_option('prefs', {'intl.accept_languages': "en"})
        browser = webdriver.Chrome(options=options)
    # Реализуем русский инетрфейс
    if language == "ru":
        options.add_experimental_option('prefs', {'intl.accept_languages': "ru"})
        browser = webdriver.Chrome(options=options)
    yield browser
    time.sleep(10)
    print("\nquit browser..")
    browser.quit()






