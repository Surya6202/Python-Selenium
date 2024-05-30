# def outer(func):
#     def wrapper(*args, **kwargs):
#         print('Good morning')
#         func(*args, **kwargs)       ## add(1, 2)
#         print('Good evening')
#     return wrapper
#
# @outer      ## add = outer(add)         ## add = wrapper_address
# def add(a, b):
#     print(a + b)
#
# add(1, 2)
# ## wrapper(1, 2)
#
# ## func --> add
# ## add --> wrapper_address
# ## *args, **kwargs --> 1, 2
import time

#------------------------------------------------------------------
import pytest
#
# @pytest.fixture()
# def greet():
#     print('Good morning')
#
# def test_login(greet):
#     print('Login executing')
#
# def test_logout(greet):
#     print('logout executing')

## collected 2 items
## test_fixtures.py::test_login Good morning       Login executing     PASSED
## test_fixtures.py::test_logout Good morning      logout executing    PASSED

#-----------------------------------------------------------------
# import pytest
#
# @pytest.fixture()
# def greet():
#     print('Good morning')
#
# def test_login(greet):
#     print('Login executing')
#
# def test_logout():
#     print('logout executing')

## collected 2 items
## test_fixtures.py::test_login Good morning       Login executing         PASSED
## test_fixtures.py::test_logout logout executing              PASSED

#--------------------------------------------------------------
# import pytest
#
# @pytest.fixture()
# def greet():
#     print('Good morning')
#
# def test_login():
#     print('Login executing')
#
# def test_logout():
#     print('logout executing')

##  the fixture will not be applied for both the functions because, we have not passed the name of the fixture as parameter

#--------------------------------------------------
## setup --> set of operations which will perform before the execution of the test function
## teardown --> set of operations which will perform after the execution of the test function

## The operations before yield will act as setup and the operations after yield will act as teardown


# @pytest.fixture()
# def greet():
#     print('Good morning')           ## setup
#     yield
#     print('Good evening')           ## teardown
#
# def test_login(greet):
#     print('Login executing')
#
# def test_logout(greet):
#     print('logout executing')

## collected 2 items
## test_fixtures.py::test_login Good morning
## Login executing
## PASSEDGood evening

## test_fixtures.py::test_logout Good morning
## logout executing
## PASSEDGood evening

#---------------------------------------------------------------------
# @pytest.fixture(autouse=True)
# def greet():
#     print('Good morning')           ## setup
#     yield
#     print('Good evening')           ## teardown
#
# def test_login():
#     print('Login executing')
#
# def test_logout():
#     print('logout executing')

## collected 2 items
## test_fixtures.py::test_login Good morning
## Login executing
## PASSEDGood evening

## test_fixtures.py::test_logout Good morning
## logout executing
## PASSEDGood evening


## When we give autouse=True,the fixture will be applied for all the test functions.
## We dont have to pass the name of the fixture as a parameter for the test functions explicitly.

## Suppose, if we want the fixtures for the selected test functions, then we should give the parameter seperately.

#-------------------------------------------------------------------
# @pytest.fixture()
# def greet():
#     print('hello everyone')
#
# class TestFacebook:
#
#     def test_login(self, greet):
#         print('login executing')
#
#     def test_logout(self, greet):
#         print('logout executing')
#
#     def test_signup(self, greet):
#         print('signup executing')

#_--------------------------------------------------------
# @pytest.fixture(autouse=True)
# def greet():
#     print('hello everyone')
#
# class TestFacebook:
#
#     def test_login(self):
#         print('login executing')
#
#     def test_logout(self):
#         print('logout executing')
#
#     def test_signup(self):
#         print('signup executing')
#
# ## collected 3 items
## test_fixtures.py::TestFacebook::test_login hello everyone
## login executing
## PASSED
## test_fixtures.py::TestFacebook::test_logout hello everyone
## logout executing
## PASSED
## test_fixtures.py::TestFacebook::test_signup hello everyone
## signup executing
## PASSED

#----------------------------------------------------------
## When we give autouse=True, the fixture will be applied for the functions as well as the class methods
# @pytest.fixture(autouse=True)
# def greet():
#     print('hello everyone')
#
# class TestFacebook:
#     def test_login(self):
#         print('login executing')
#
# def test_logout():
#     print('logout executing')

## collected 2 items
## test_fixtures.py::TestFacebook::test_login hello everyone
## login executing
## PASSED
## test_fixtures.py::test_logout hello everyone
## logout executing
## PASSED

#-----------------------------------------------------
# @pytest.fixture(scope='class', autouse=True)
# def greet():
#     print('hello everyone')
#
# class TestFacebook:
#
#     def test_login(self):
#         print('login executing')
#
#     def test_logout(self):
#         print('logout executing')
#
#     def test_signup(self):
#         print('signup executing')

## collected 3 items
## test_fixtures.py::TestFacebook::test_login hello everyone
## login executing          PASSED
## test_fixtures.py::TestFacebook::test_logout logout executing         PASSED
## test_fixtures.py::TestFacebook::test_signup signup executing         PASSED

#---------------------------------------------------------------------------
# @pytest.fixture(autouse=True)
# def greet():
#     print('hello everyone')
#
# def test_addition():
#     print('addition executing')
#
# class TestFacebook:
#
#     def test_login(self):
#         print('login executing')
#
#     def test_logout(self):
#         print('logout executing')
#
# class TestSample:
#
#     def test_signup(self):
#         print('signup executing')
#
#     def test_registration(self):
#         print('registartion executing')

## collected 5 items
## test_fixtures.py::test_addition hello everyone
##                                 addition executing          PASSED
## test_fixtures.py::TestFacebook::test_login hello everyone
##                                 login executing         PASSED
## test_fixtures.py::TestFacebook::test_logout hello everyone
##                                 logout executing        PASSED
## test_fixtures.py::TestSample::test_signup hello everyone
##                                 signup executing        PASSED
## test_fixtures.py::TestSample::test_registration hello everyone
##                                 registartion executing  PASSED

#---------------------------------------------------
## When we gice scope='class', the fixture will be applied once before the execution of the test functions
## i.e., fixture will not  be applied for the test methods individually.
## By default, scope='func'

# @pytest.fixture(scope='class', autouse=True)
# def greet():
#     print('hello everyone')
#
# class TestFacebook:
#
#     def test_login(self):
#         print('login executing')
#
#     def test_logout(self):
#         print('logout executing')
#
# class TestSample:
#
#     def test_signup(self):
#         print('signup executing')
#
#     def test_registration(self):
#         print('registartion executing')

#------------------------------------------------------------------
# @pytest.fixture(autouse=True, scope='class')
# def greet():
#     print('hello everyone')
#     yield
#     print('bye')
#
# class TestFacebook:
#
#     def test_login(self):
#         print('login executing')
#
#     def test_logout(self):
#         print('logout executing')
#
# def test_addition():
#     print('addition executing')

#-----------------------------------------------------------------------
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=opts)
#
# @pytest.fixture()
# def launching_url():
#     driver.get('https://demowebshop.tricentis.com/')
#     time.sleep(2)
#
# def test_register(launching_url):
#     driver.find_element('xpath', '//a[text()="Register"]').click()
#     time.sleep(3)
#
# def test_login(launching_url):
#     driver.find_element('xpath', '//a[text()="Log in"]').click()

#-----------------------------------------------------------------
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# @pytest.fixture()
# def launching_url():
#     driver = webdriver.Chrome(options=opts)
#     driver.get('https://demowebshop.tricentis.com/')
#     time.sleep(2)
#     yield driver
#     driver.close()
#
# def test_register(launching_url):       ## launching_url --> driver
#     launching_url.find_element('xpath', '//a[text()="Register"]').click()
#     time.sleep(3)
#
# def test_login(launching_url):
#     launching_url.find_element('xpath', '//a[text()="Log in"]').click()
#     time.sleep(3)









































































































