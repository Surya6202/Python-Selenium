'''
passing the parameters for the test functions:

To pass the parameters for the test functions, we have to decorate the function with
@pytest.mark.parametrize("formal args", [(), ()])
        formal args should be in string format, actual args in list of tuples

'''
import time

import pytest


#----------------------------------------------------------------
# import pytest
#
# @pytest.mark.parametrize('a, b', [(10, 20), (11, 22), (9, 65), (-98, 678)])
# def test_add(a, b):
#     print(a + b)

## collected 4 items
## test_parameterize.py::test_add[10-20] 30                PASSED
## test_parameterize.py::test_add[11-22] 33                PASSED
## test_parameterize.py::test_add[9-65] 74                 PASSED
## test_parameterize.py::test_add[-98-678] 580             PASSED

#---------------------------------------------------------

# import pytest
#
# @pytest.mark.parametrize('a, b, c', [(10, 20), (11, 22)])
# def test_add(a, b):
#     print(a + b)

## The above code will give us error, because the number of formal args and actual args are not same

#-----------------------------------------------------------

# class TestCalculator:
#
#     @pytest.mark.parametrize('a, b', [(1, 2), (2, 3)])
#     def test_addition(self, a, b):
#         print(a + b)
#
#     @pytest.mark.parametrize('a, b', [(11, 2), (2, 30)])
#     def test_subtraction(self, a, b):
#         print(a - b)

## collected 4 items
## test_parameterize.py::TestCalculator::test_addition[1-2] 3          PASSED
## test_parameterize.py::TestCalculator::test_addition[2-3] 5          PASSED
## test_parameterize.py::TestCalculator::test_subtraction[11-2] 9      PASSED
## test_parameterize.py::TestCalculator::test_subtraction[2-30] -28    PASSED

#-------------------------------------------------------------------

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
#
# @pytest.mark.parametrize("username, password", [('standard_user', 'secret_sauce'), ('locked_out_user', 'secret_sauce'), ('problem_user', 'secret_sauce')])
# def test_saucedemo(username, password):
#     driver = webdriver.Chrome(options=opts)
#     driver.get('https://www.saucedemo.com/')
#     time.sleep(2)
#     driver.find_element('xpath', '//input[@id="user-name"]').send_keys(username)
#     time.sleep(2)
#     driver.find_element('xpath', '//input[@id="password"]').send_keys(password)
#     time.sleep(4)


#-----------------------------------------------------------------------------

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=opts)
wait_obj = WebDriverWait(driver, 30)

@pytest.mark.parametrize("username, password", [('standard_user', 'secret_sauce'), ('locked_out_userrr', 'secret_sauce'), ('problem_user', 'secret_sauce')])
def test_saucedemo(username, password):
    driver.get('https://www.saucedemo.com/')
    time.sleep(2)
    driver.find_element('xpath', '//input[@id="user-name"]').send_keys(username)
    time.sleep(2)
    driver.find_element('xpath', '//input[@id="password"]').send_keys(password)
    time.sleep(2)
    driver.find_element('xpath', '//input[@id="login-button"]').click()

    backpack = driver.find_element('xpath', '//div[text()="Sauce Labs Backpack"]')

    # if wait_obj.until(expected_conditions.visibility_of(backpack)):
    #     pass
    # else:
    #     raise Exception('Invalid credentials')

    ## OR

    assert wait_obj.until(expected_conditions.visibility_of(backpack))





























