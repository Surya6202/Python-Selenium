from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
import pytest


def browser_setup(browser_name: str) -> WebDriver|None:
    browser = browser_name.capitalize()
    if browser not in ['Chrome', 'Edge', 'Firefox']:
        print("Invalid browser")
    if browser.__eq__("Chrome"):
        return webdriver.Chrome()
    elif browser.__eq__("Edge"):
        return webdriver.Edge()
    elif browser.__eq__("Firefox"):
        return webdriver.Firefox()

# @pytest.mark.parametrize('name',('Chrome','Edge','Firefox'))
@pytest.fixture()
def pre_and_postcondition(name):
    driver = browser_setup(name)
    if not isinstance(driver, WebDriver):
        pass
    yield
    driver.quit()

