# import time
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=opts)
#
# def test_launch_webpage():
#     driver.get('https://demowebshop.tricentis.com/')
#     time.sleep(2)
#
# def test_click_on_register():
#     driver.find_element('xpath', '//a[text()="Register"]').click()
#     time.sleep(2)
#
# def test_click_on_gender():
#     driver.find_element('xpath', '//input[@id="gender-male"]').click()
#
# def test_first_name():
#     driver.find_element('xpath', '//input[@id="FirstName"]').send_keys('Narendra')
#
# def test_lastname():
#     driver.find_element('xpath', '//input[@id="LastName"]').send_keys('Modi')
#
# def test_email():
#     driver.find_element('xpath', '//input[@id="Email"]').send_keys('narendra_modi@gmail.com')
#
# def test_password():
#     driver.find_element('xpath', '//input[@id="Password"]').send_keys('Narendra@123')
#
# def test_confirm_password():
#     driver.find_element('xpath', '//input[@id="ConfirmPassword"]').send_keys('Narendra@123')
#
import time

#------------------------------------------------------------------------------
# def spam():
#     print('In spam')
#
# def display():
#     print('In display')
#
# spam()
# display()
#
# ## call the functions

#------------------------------------------------------------------------
# def test_spam():
#     print('In spam')
#
# def test_display():
#     print('In display')

## collected 2 items
## test_basic.py::test_spam In spam                    PASSED
## test_basic.py::test_display In display              PASSED

#----------------------------------------------------------------------
# def test_login():
#     print('Login executing')
#
# def logout():
#     print('logout executing')


## collected 1 item
## test_basic.py::test_login Login executing       PASSED
## Logout will not get executed because, logout is not following the pytest convention.

#---------------------------------------------------------------------
# class TestSample:
#
#     def test_login(self):
#         print('Login executing')
#
#     def test_logout(self):
#         print('logout executing')

## collected 2 items
## test_basic.py::TestSample::test_login Login executing           PASSED
## test_basic.py::TestSample::test_logout logout executing         PASSED

#---------------------------------------------------------------------
# class Sample:
#
#     def test_login(self):
#         print('Login executing')
#
#     def test_logout(self):
#         print('logout executing')
#
# ## collected 0 items
# ## Because, the classname is not following the pytest convention

#----------------------------------------------------------------------
# class TestFacebook:
#
#     def test_login(self):
#         print('login executing')
#
#     def signup(self):
#         print('signup executing')
#
#     def test_registration(self):
#         print('registration executing')
#
#     def test_logout(self):
#         print('logout executing')

## collected 3 items
## test_basic.py::TestFacebook::test_login login executing                 PASSED
## test_basic.py::TestFacebook::test_registration registration executing   PASSED
## test_basic.py::TestFacebook::test_logout logout executing               PASSED

#---------------------------------------------------------------
# ## The failure of one testcase will not affect the other testcases.
#
# def test_login():
#     prin('login executing')
#
# def test_logout():
#     print('logout executing')
#
# ## collected 2 items
# ## test_basic.py::test_login FAILED
# ## test_basic.py::test_logout logout executing          PASSED

#-------------------------------------------------------------------
# def test_login():
#     print('login executing')
#     def test_signup():
#         print('signup executing')


## collected 1 item
## test_basic.py::test_login login executing               PASSED
## pytest can only recognize the outer test function, but not the inner test function

#---------------------------------------------------------------------
# a = 10
# b = 20
#
# def test_addition():
#     print(a + b)
#
# def test_subtraction():
#     print(a - b)

## collected 2 items
## test_basic.py::test_addition 30             PASSED
## test_basic.py::test_subtraction -10         PASSED

#-------------------------------------------------------------------
# def test_addition(a, b):
#     print(a + b)
#
# test_addition(1, 2)

## collected 1 item
## test_basic.py::test_addition ERROR

## Should not pass parameters for the test functions

#---------------------------------------------------------------------
# class TestCalculator:
#
#     a = 10
#     b = 20
#
#     def test_add(self):
#         print(self.a + self.b)
#
#     def test_sub(self):
#         print(self.a - self.b)

## collected 2 items
## test_basic.py::TestCalculator::test_add 30          PASSED
## test_basic.py::TestCalculator::test_sub -10         PASSED

#_-----------------------------------------------------
# class TestCalculator:
#
#     def test_add(self, a, b):
#         print(a + b)
#
# cal1 = TestCalculator()
# cal1.test_add(1, 2)

## collected 1 item
## test_basic.py::TestCalculator::test_add ERROR
## cant create objects for the testclasses

#------------------------------------------------------
# class TestCalculator:
#
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def test_add(self):
#         print(self.a + self.b)

## collected 0 items
## It will give Warning
## Cannot define __init__ for the test classes

#-------------------------------------------------------
# class SampleTest:
#
#     def test_spam(self):
#         print('In spam')

## collected 0 items
## Because, classname is not following the pytest convention

#---------------------------------------------------------------------

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=opts)

def test_launch_webpage():
    driver.get('https://www.saucedemo.com/')
    time.sleep(2)

def test_username():
    driver.find_element('xpath', '//input[@id="user-name"]').send_keys('standard_user')
    time.sleep(2)

def test_password():
    driver.find_element('xpath', '//input[@id="password"]').send_keys('secret_sauce')
    time.sleep(2)

def test_click_on_login():
    driver.find_element('xpath', '//input[@id="login-button"]').click()
    time.sleep(3)

def test_click_on_openmenu():
    driver.find_element('xpath', '//button[text()="Open Menu"]').click()
    time.sleep(2)

def test_click_logout():
    driver.find_element('xpath', '//a[text()="Logout"]').click()

#-------------------------------------------------------------------











































































































