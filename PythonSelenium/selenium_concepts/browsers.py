from configparser import ConfigParser
from time import sleep
from utilities import chrome_options, edge_options
from selenium import webdriver
from selenium.common import NoSuchDriverException


def get_data(section, key):
    config = ConfigParser()
    config.read(r'D:\Programming\Python\PythonSelenium\files\test_data.ini')
    return config.get(section, key)


for i in range(1, 5):
    browser = get_data('browsers', 'browser')

    if browser == 'chrome':
        driver = webdriver.Chrome(chrome_options)
        print('chrome launched')
        driver.quit()

    elif browser == 'edge':
        driver = webdriver.Edge(edge_options)
        print('edge launched')
        driver.quit()

    elif browser == 'firefox':
        driver = webdriver.Firefox()
        driver.maximize_window()
        print('firefox launched')
        driver.quit()

    elif browser == 'safari':
        try:
            driver = webdriver.Safari()
            driver.quit()
        except NoSuchDriverException:
            print("safari not launched")
        finally:
            print('NoSuchDriverException handled')
    sleep(2)