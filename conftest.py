import pytest
from selenium import webdriver
from Utilities.ReadConfig import ReadConfig

def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture(scope="function")
def setup(request):
    browser = request.config.getoption("--browser")
    if browser == "Chrome":
        print("Running in Chrome")
        driver = webdriver.Chrome()
    elif browser == "Edge":
        print("Running in Edge")
        driver = webdriver.Edge()
    else:
        driver = webdriver.Chrome()

    driver.maximize_window()

    driver.get(ReadConfig().get_application_url())
    request.cls.driver = driver
    yield driver
    driver.quit()