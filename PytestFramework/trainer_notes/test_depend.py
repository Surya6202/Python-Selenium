'''
dependency = To make testcases dependent on each other, we use dependencies

SYNTAX : @pytest.mark.dependency() --> independent testcase
         @pytest.mark.dependency(depends=['independent testcase name'])

If the independent testcase executes, then dependent will also execute
If the independent testcase fails, the dependent testcase will be skipped


To make one testcase dependent on multiple testcases
@pytest.mark.dependency(depends=['testcase1', 'testcase2', 'testcase3',...])
'''
#-----------------------------------------------------------------
import pytest

# @pytest.mark.dependency()
# def test_login():                   ## independent testcase
#     print('login executing')
#
# @pytest.mark.dependency(depends=["test_login"])
# def test_logout():                  ## dependent on test_login
#     print('logout executing')

## Here test_logout is depending in test_login.
## If the test_login works without any fail, logout will also work.

#--------------------------
# @pytest.mark.dependency()
# def test_login():                   ## independent testcase
#     assert 10==100
#
# @pytest.mark.dependency(depends=["test_login"])
# def test_logout():                  ## dependent on test_login
#     print('logout executing')

## collected 2 items
## test_depend.py::test_login FAILED
## test_depend.py::test_logout SKIPPED (test_logout depends on test_login)

## In this example, test_login fails, if the independent test function fails, the dependent test func will be skipped

#--------------------------------------------------------------
import time
import pytest

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=opts)
wait_obj = WebDriverWait(driver, 30)

@pytest.mark.dependency()
def test_login():
    driver.get('https://www.saucedemo.com/')
    time.sleep(2)
    driver.find_element('xpath', '//input[@id="user-name"]').send_keys('standard_userrr')
    time.sleep(2)
    driver.find_element('xpath', '//input[@id="password"]').send_keys('secret_sauce')
    time.sleep(2)
    driver.find_element('xpath', '//input[@id="login-button"]').click()

    backpack = driver.find_element('xpath', '//div[text()="Sauce Labs Backpack"]')
    assert wait_obj.until(expected_conditions.visibility_of(backpack))

@pytest.mark.dependency(depends=['test_login'])
def test_logout():
    driver.find_element('xpath', '//button[text()="Open Menu"]').click()
    time.sleep(2)
    driver.find_element('xpath', '//a[text()="Logout"]').click()
