'''
pytest markers
There are two types of markers
    i) inbuilt marker :
            i) skip
            ii) skipif
            iii) parameterize
            iv) xfail
    ii) custom marker : To group the testcases.
                We give the names for the testcases by decorating them with @pytest.mark.name
'''
import time

#---------------------------------------------------------------------------------
import pytest

# @pytest.mark.sanity
# def test_add():
#     print('Addition executing')
#
# @pytest.mark.smoke
# def test_sub():
#     print('Subtraction executing')
#
# @pytest.mark.sanity
# def test_mul():
#     print('Multiplication executing')
#
# @pytest.mark.regression
# def test_div():
#     print('Division executing')


## pytest test_markerss.py -vs -m sanity
## collected 4 items / 2 deselected / 2 selected
## test_markerss.py::test_add Addition executing           PASSED
## test_markerss.py::test_mul Multiplication executing     PASSED


## pytest test_markerss.py -vs -m smoke
## collected 4 items / 3 deselected / 1 selected
## test_markerss.py::test_sub Subtraction executing        PASSED

#-------------------------------------------------------------------
## NOTE : To execute all the testcases, pytest test_filename.py -vs

#----------------------------------------------------------------------

# @pytest.mark.smoke
# def test_add():
#     print('Addition executing')
#
# @pytest.mark.smoke
# def test_sub():
#     print('Subtraction executing')
#
# @pytest.mark.sanity
# def test_mul():
#     print('Multiplication executing')
#
# @pytest.mark.regression
# def test_div():
#     print('Division executing')

## pytest test_markerss.py -vs -m "sanity or regression" --> test_mul and test_div will execute
## pytest test_markerss.py -vs -m "sanity and regression" --> 4 deselected.
## Because we donot have any testcase which is both sanity as well as regression

#--------------------------------------------------------------------------------
# @pytest.mark.smoke
# def test_add():
#     print('Addition executing')
#
# @pytest.mark.regression
# @pytest.mark.smoke
# def test_sub():
#     print('Subtraction executing')
#
# @pytest.mark.sanity
# def test_mul():
#     print('Multiplication executing')
#
# @pytest.mark.regression
# def test_div():
#     print('Division executing')

#------------------------------------------------------------------------
# @pytest.mark.smoke
# def test_login():
#     print('login executing')
#
# @pytest.mark.smoke
# @pytest.mark.sanity
# def test_logout():
#     print('logout executing')
#
# @pytest.mark.sanity
# def test_signup():
#     print('signup executing')
#
# @pytest.mark.smoke
# @pytest.mark.regression
# def test_reg():
#     print('registration executing')

#-------------------------------------------------------------
# @pytest.mark.smoke
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
#     def test_reg(self):
#         print('registration executing')

## in terminal --> pytest test_markerss.py -vs -m smoke --> All the testcases will execute

#------------------------------------------------------------
# class TestFacebook:
#
#     @pytest.mark.smoke
#     def test_login(self):
#         print('login executing')
#
#     @pytest.mark.sanity
#     def test_logout(self):
#         print('logout executing')
#
#     @pytest.mark.regression
#     def test_signup(self):
#         print('signup executing')
#
#     @pytest.mark.smoke
#     def test_reg(self):
#         print('registration executing')

#--------------------------------------------------------------
# @pytest.mark.performance
# class TestFacebook:
#
#     @pytest.mark.smoke
#     def test_login(self):
#         print('login executing')
#
#     @pytest.mark.sanity
#     def test_logout(self):
#         print('logout executing')
#
#     @pytest.mark.regression
#     def test_signup(self):
#         print('signup executing')
#
#     @pytest.mark.regression
#     @pytest.mark.smoke
#     def test_reg(self):
#         print('registration executing')
#
# ## test_login is both performance and smoke
# ## test_logout is both performance and sanity
# ## test_sighup is both performance and regression
# ## test_reg is both performance, smoke and regression
#
# ## pytest test_markerss.py -vs -m "sanity or regression" --> test_logout, test_signup and test_reg will execute
# ## pytest test_markerss.py -vs -m "smoke or regression" --> test_login, test_signup and test_reg will execute

#----------------------------------------------------------------------------

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=opts)
#
# driver.get('https://demowebshop.tricentis.com/')
# time.sleep(2)
#
# @pytest.mark.register
# class TestDemoRegister:
#
#     def test_register(self):
#         driver.find_element('xpath', '//a[text()="Register"]').click()
#         time.sleep(3)
#
#     def test_gender(self):
#         driver.find_element('xpath', '//input[@id="gender-male"]').click()
#         time.sleep(2)
#
#     def test_fname(self):
#         driver.find_element('xpath', '//input[@id="FirstName"]').send_keys('Rahul')
#         time.sleep(2)
#
#     def test_lname(self):
#         driver.find_element('xpath', '//input[@id="LastName"]').send_keys('Dravid')
#         time.sleep(3)
#
# @pytest.mark.login
# class TestDemoLogin:
#
#     def test_login(self):
#         driver.find_element('xpath', '//a[text()="Log in"]').click()
#         time.sleep(2)
#
#     def test_email(self):
#         driver.find_element('xpath', '//input[@id="Email"]').send_keys('rahuldravid@gmail.com')
#         time.sleep(2)
#
#     def test_pwd(self):
#         driver.find_element('xpath', '//input[@id="Password"]').send_keys('rahul1234')

#---------------------------------------------------------------------------------
## inbuilt markers

## skip : To skip the testcase without any condition, we use skip

# import pytest
#
# def test_login():
#     print('login executing')
#
# @pytest.mark.skip
# def test_logout():
#     print('logout executing')
#
# def test_signup():
#     print('signup executing')

## collected 3 items
## test_markerss.py::test_login login executing                    PASSED
## test_markerss.py::test_logout SKIPPED (unconditional skip)
## test_markerss.py::test_signup signup executing                  PASSED

#----------------------------------------------------------------------
# def test_login():
#     print('login executing')
#
# @pytest.mark.skip
# def test_logout():
#     print('logout executing')
#
# @pytest.mark.skip
# def test_signup():
#     print('signup executing')

## collected 3 items
## test_markerss.py::test_login login executing
## PASSED
## test_markerss.py::test_logout SKIPPED (unconditional skip)
## test_markerss.py::test_signup SKIPPED (unconditional skip)

#--------------------------------------------------------------------

# @pytest.mark.smoke
# def test_login():
#     print('login executing')
#
# @pytest.mark.skip
# @pytest.mark.smoke
# def test_logout():
#     print('logout executing')
#
# @pytest.mark.skip
# def test_signup():
#     print('signup executing')

## collected 3 items
## test_markerss.py::test_login login executing                PASSED
## test_markerss.py::test_logout SKIPPED (unconditional skip)
## test_markerss.py::test_signup SKIPPED (unconditional skip)

#------------------------------------------------------------
# @pytest.mark.smoke
# def test_login():
#     print('login executing')
#
# @pytest.mark.smoke
# @pytest.mark.skip
# def test_logout():
#     print('logout executing')
#
# @pytest.mark.skip
# def test_signup():
#     print('signup executing')

## collected 3 items
## test_markerss.py::test_login login executing                        PASSED
## test_markerss.py::test_logout SKIPPED (unconditional skip)
## test_markerss.py::test_signup SKIPPED (unconditional skip)

#-----------------------------------------------------------
# @pytest.mark.smoke
# def test_login():
#     print('login executing')
#
# @pytest.mark.smoke
# @pytest.mark.skip
# def test_logout():
#     print('logout executing')
#
# @pytest.mark.skip
# def test_signup():
#     print('signup executing')

## collected 3 items / 1 deselected / 2 selected
## test_markerss.py::test_login login executing                    PASSED
## test_markerss.py::test_logout SKIPPED (unconditional skip)

#------------------------------------------------------------------
# @pytest.mark.skip
# class TestGoogle:
#
#     def test_gmail(self):
#         print('gmail executing')
#
#     def test_chrome(self):
#         print('chrome executing')
#
#     def test_gtalk(self):
#         print('gtalk executing')
#
#     def test_drive(self):
#         print('drive executing')

## collected 4 items
## test_markerss.py::TestGoogle::test_gmail SKIPPED (unconditional skip)
## test_markerss.py::TestGoogle::test_chrome SKIPPED (unconditional skip)
## test_markerss.py::TestGoogle::test_gtalk SKIPPED (unconditional skip)
## test_markerss.py::TestGoogle::test_drive SKIPPED (unconditional skip)

#-----------------------------------------------------------------------
# @pytest.mark.smoke
# class TestGoogle:
#
#     @pytest.mark.skip(reason="unwanted testcase")
#     def test_gmail(self):
#         print('gmail executing')
#
#     @pytest.mark.sanity
#     def test_chrome(self):
#         print('chrome executing')
#
#     @pytest.mark.regression
#     def test_gtalk(self):
#         print('gtalk executing')
#
#     @pytest.mark.sanity
#     @pytest.mark.skip
#     def test_drive(self):
#         print('drive executing')

## In terminal --> pytest test_markerss.py -vs -m "smoke and sanity"
## collected 4 items / 2 deselected / 2 selected
## test_markerss.py::TestGoogle::test_chrome chrome executing                     PASSED
## test_markerss.py::TestGoogle::test_drive SKIPPED (unconditional skip)

#-----------------------------------------------------------------------

## skipif : To skip the testcase based on condition
## Syntax : @pytest.mark.skipif(condition, reason)
## Both condition and reason are mandatory
## The testcase will be skipped only if the condition is true
#
# a = 10
#
# @pytest.mark.skipif(a==20, reason='unnecessary testcase')
# def test_login():
#     print('login executing')
#
# @pytest.mark.skipif(a==10, reason='unnecessary testcase')
# def test_logout():
#     print('logout executing')
#
# def test_signup():
#     print('signup executing')


## collected 3 items
## test_markerss.py::test_login login executing                    PASSED
## test_markerss.py::test_logout SKIPPED (unnecessary testcase)
## test_markerss.py::test_signup signup executing                  PASSED

#-----------------------------------------------------------------------------

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# @pytest.mark.skipif('demo' not in 'https://demowebshop.tricentis.com/', reason='Unnecessary')
# def test_launch1():
#     driver = webdriver.Chrome(options=opts)
#     driver.get('https://demowebshop.tricentis.com/')
#     time.sleep(3)
#
# @pytest.mark.skipif('demo' not in 'https://www.myntra.com/', reason='Unnecessary')
# def test_launch2():
#     driver = webdriver.Chrome(options=opts)
#     driver.get('https://www.myntra.com/')
#     time.sleep(3)
#
# @pytest.mark.skipif('demo' not in 'https://www.saucedemo.com/', reason='Unnecessary')
# def test_launch3():
#     driver = webdriver.Chrome(options=opts)
#     driver.get('https://www.saucedemo.com/')
#     time.sleep(3)

## collected 3 items
## test_markerss.py::test_launch1          PASSED
## test_markerss.py::test_launch2 SKIPPED (Unnecessary)
## test_markerss.py::test_launch3          PASSED


#--------------------------------------------------------------------
## xfail
# import pytest
#
# def test_login():
#     print('login executing')
#
# @pytest.mark.xfail
# def test_logout():
#     print('logout executing')
#
# ## collected 2 items
# ## test_markerss.py::test_login login executing            PASSED
# ## test_markerss.py::test_logout logout executing          XPASS












