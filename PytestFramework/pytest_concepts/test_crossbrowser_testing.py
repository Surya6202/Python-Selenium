import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver


def browser_setup(browser_name: str) -> WebDriver|str:
    browser = browser_name.capitalize()
    if browser.__eq__("Chrome"):
        return webdriver.Chrome()
    elif browser.__eq__("Edge"):
        return webdriver.Edge()
    elif browser.__eq__("Firefox"):
        return webdriver.Firefox()
    else:
        return "Invalid browser"


@pytest.mark.parametrize('name', ['safari','chrome'])
def testdemo(name):
    driver = browser_setup(name)
    if not isinstance(driver,WebDriver):
        print(driver)
        quit()

    driver.get('https://www.facebook.com/')
    driver.quit()