"""
import pytest

# Pytest markers:
# It provides a flexible way to manage and execute tests based on their attributes, making test suites more efficient
# and maintainable.
# In automation, it's used to group the test cases or skip test cases in test execution.
# Pytest markers is of two types:
# 1) Inbuilt markers.
# 2) Custom/ User-defined markers.

# Inbuilt markers:
# It's used to set various features to the test functions.
# It provides markers such as skip, skipif, xfail, parametrize, filterwarnings and usefixtures.

# Note:
# A test is not relevant for some time due to some reasons.
# A new feature is being implemented and we already added a test for that feature.
# In this scenarios, we can xfail the test or skip the tests.

# 1) skip:
# Skipping a test means that the test will not be executed.
# It's used to skip the test functions from the test execution by marking it with the skip decorator to
# the test function and We can do this by using the following marker − '@pytest.mark.skip'.

# 2) skipif:
# It's used to skip the test functions from the test execution based on the condition and it's done by
# marking it with skipif decorator to the test function.
# We can do this by using the following marker − '@pytest.mark.skipif'.

# 3) xfail:
# It's used to mark a test function whixh is expected to be failed.
# We can do this by using the following marker − '@pytest.mark.xfail'.
# It'll execute the xfailed test, but it will not be considered as part failed or passed tests.
# Details of these tests will not be printed even if the test fails
# If it's passed, we'll get a message like 'xpass' and if it fails, we'll get a message like 'xfail' and it'll be
# ignored and even we can pass conditions also.
# We can also specify the reason for failure by using reason parameter.
# We can also specify the error or exception by using raises parameter.

# 4) parametrize:
# It allows to easily parametrize test functions.
# Parameterizing of a test is done to run the test against multiple sets of inputs.
# We can do this by using the following marker − '@pytest.mark.parametrize'.
# Parameterizing of a test is done to run the test against multiple sets of inputs.
# Based on the specified inputs, it'll execute single time or mutliple times

# 5) usefixtures:
# It's used to apply the created fixtures to the test functions, classes and files.

# @pytest.mark.skip
# def test_register():
#     print('Account registration')
#
#
# def test_login():
#     print('Logged in')
#
#
# @pytest.mark.skipif(reason="not used in this execution")
# def test_search_product():
#     print('product is found')
#
#
# @pytest.mark.xfail
# def test_add_product():
#     print('product added')
#
#
# @pytest.mark.xfail
# def test_purchase_product():
#     assert False
#
#
# def test_logout():
#     print('logged out')
#

# collected 6 items
# test_pymarkers.py::test_register SKIPPED (unconditional skip)                                  [ 16%]
# test_pymarkers.py::test_login PASSED                                                           [ 33%]
# test_pymarkers.py::test_search_product SKIPPED (not used in this execution)                    [ 50%]
# test_pymarkers.py::test_add_product XPASS                                                      [ 66%]
# test_pymarkers.py::test_purchase_product XFAIL                                                 [ 83%]
# test_pymarkers.py::test_logout PASSED                                                          [100%]
# ================== 2 passed, 2 skipped, 1 xfailed, 1 xpassed in 0.15s =================


# @pytest.mark.parametrize('name', ['Surya', 'Mithra Nandan', 'Rajanandini', 'Nayani'])
# def test_names(name):
#     print(name)
#

# collected 4 items
# test_pymarkers.py::test_names[Surya] PASSED                                                            [ 25%]
# test_pymarkers.py::test_names[Mithra Nandan] PASSED                                                    [ 50%]
# test_pymarkers.py::test_names[Rajanandini] PASSED                                                      [ 75%]
# test_pymarkers.py::test_names[Nayani] PASSED                                                           [100%]
# =============== 4 passed in 0.08s ==================

# @pytest.fixture()
# def greet():
#     print('Hello')
#     yield
#     print('Jai sree krishna')
#
#
# @pytest.mark.usefixtures('greet')
# @pytest.mark.parametrize('name', ['Surya', 'Santhosh'])
# def test_greetings(name):
#     print(name)

# collected 2 items
# test_pymarkers.py Hello
# Surya
# .Jai sree krishna
# Hello
# Santhosh
# .Jai sree krishna
# ==================== 2 passed in 0.03s ====================

# Custom/ User-defined Marker:
# In pytest, We can mark any test functions with user-defined markers and this marker name can be anything..
# By this markers, We can group the test cases.
# We can also perform group execution.
# This markers will execute successfully but it raises certain warnings.
# We can overcome this warnings by registering this markers in the configuration file and save the file in
# the same package.
# The file extension for configuration file is 'filename.ini' and file name should be 'pytest'.

# @pytest.mark.tollywood
# def test_hero():
#     print('prabhas')

# collected 1 item
# test_pymarkers.py .               [100%]
# =============== warnings summary ========================
# test_pymarkers.py:110
# D:\Programming\Python\PythonSelenium\pytest_framework\test_pymarkers.py:110: PytestUnknownMarkWarning:
# Unknown pytest.mark.tollywood - is this a typo?  You can register custom marks to avoid this warning - for details,
# see https://docs.pytest.org/en/stable/how-to/mark.html
# @pytest.mark.tollywood
# -- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
# ============= 1 passed, 1 warning in 0.05s =====================

# To avoid this warning, We need to register that marker in configuration file.

# @pytest.mark.tollywood
# def test_hero():
#     print('prabhas')
# collected 1 item
# test_pymarkers.py .                                  [100%]
# ============== 1 passed in 0.04s ===================================

# Grouping the test functions and executing it by the group names.
# class Test_Facebook:
#
#     @pytest.mark.smoke
#     @pytest.mark.functional
#     def test_login(self):
#         print('logged in')
#
#     @pytest.mark.functional
#     def test_add_friend(self):
#         print('added friend')
#
#     @pytest.mark.functional
#     def test_edit_profile(self):
#         print('profile edited')
#
#     @pytest.mark.integration
#     def test_dp_changed(self):
#         print('dp changed')
#
#     @pytest.mark.integration
#     def test_bio_changed(self):
#         print('Bio changed')
#
#     @pytest.mark.smoke
#     @pytest.mark.functional
#     def test_logout(self):
#         print('logged out')
#
#
# class Test_Instagram:
#
#     @pytest.mark.smoke
#     @pytest.mark.functional
#     def test_login(self):
#         print('logged in')
#
#     @pytest.mark.functional
#     def test_add_follower(self):
#         print('added follower')
#
#     @pytest.mark.functional
#     def test_edit_profile(self):
#         print('profile edited')
#
#     @pytest.mark.integration
#     def test_dp_changed(self):
#         print('dp changed')
#
#     @pytest.mark.integration
#     def test_bio_changed(self):
#         print('Bio changed')
#
#     @pytest.mark.smoke
#     @pytest.mark.functional
#     def test_logout(self):
#         print('logged out')

# Functional:
# collected 12 items / 4 deselected / 8 selected
# test_pymarkers.py::Test_Facebook::test_login PASSED                                      [ 12%]
# test_pymarkers.py::Test_Facebook::test_add_friend PASSED                                 [ 25%]
# test_pymarkers.py::Test_Facebook::test_edit_profile PASSED                               [ 37%]
# test_pymarkers.py::Test_Facebook::test_logout PASSED                                     [ 50%]
# test_pymarkers.py::Test_Instagram::test_login PASSED                                     [ 62%]
# test_pymarkers.py::Test_Instagram::test_add_follower PASSED                              [ 75%]
# test_pymarkers.py::Test_Instagram::test_edit_profile PASSED                              [ 87%]
# test_pymarkers.py::Test_Instagram::test_logout PASSED                                    [100%]
# =============== 8 passed, 4 deselected in 0.06s ====================

# Integration:
# collected 12 items / 8 deselected / 4 selected
# test_pymarkers.py::Test_Facebook::test_dp_changed PASSED                                 [ 25%]
# test_pymarkers.py::Test_Facebook::test_bio_changed PASSED                                [ 50%]
# test_pymarkers.py::Test_Instagram::test_dp_changed PASSED                                [ 75%]
# test_pymarkers.py::Test_Instagram::test_bio_changed PASSED                               [100%]
# ================ 4 passed, 8 deselected in 0.04s =====================

# Smoke:
# collected 12 items / 8 deselected / 4 selected
# test_pymarkers.py::Test_Facebook::test_login PASSE                                       [ 25%]
# test_pymarkers.py::Test_Facebook::test_logout PASSED                                     [ 50%]
# test_pymarkers.py::Test_Instagram::test_login PASSED                                     [ 75%]
# test_pymarkers.py::Test_Instagram::test_logout PASSED                                    [100%]
# ============= 4 passed, 8 deselected in 0.08s =========================

# Script group execution:

# from selenium import webdriver
# from selenium.webdriver import ActionChains
# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.support.wait import WebDriverWait
#
# options = webdriver.ChromeOptions()
# options.add_experimental_option('detach', True)
# options.add_argument('--start-maximized')
#
#
# @pytest.fixture()
# def pre_and_postcondition():
#     global driver, actions, wait
#     driver = webdriver.Chrome(options=options)
#     driver.implicitly_wait(20)
#     wait = WebDriverWait(driver, 30)
#     actions = ActionChains(driver)
#     yield
#     driver.minimize_window()
#     driver.quit()
#
#
# @pytest.mark.usefixtures('pre_and_postcondition')
# @pytest.mark.functional
# @pytest.mark.parametrize(['url', 'email', 'password'],
#                          [('https://www.facebook.com', 'surya123@gmail.com', 'Surya@123')])
# def test_fb_login(url, email, password):
#     driver.get(url)
#     driver.find_element('id', 'email').send_keys(email)
#     driver.find_element('id', 'pass').send_keys(password)
#     driver.find_element('name', 'login').submit()
#
#
# @pytest.mark.usefixtures('pre_and_postcondition')
# @pytest.mark.parametrize('url', ['https://www.makemytrip.com/'])
# @pytest.mark.integration
# def test_select_date(url):
#     driver.get(url)
#     actions.pause(5).click().perform()
#     driver.find_element('xpath', '//span[text() = "Departure"]').click()
#     month = driver.find_element('xpath', '(//div[@class = "DayPicker-Caption"]/div)[1]').text
#     while not month.__eq__('February 2024'):
#         driver.find_element('xpath', '//div[@class = "DayPicker-NavBar"]/child::span[contains(@class, "next")]').click()
#         month = driver.find_element('xpath', '(//div[@class = "DayPicker-Caption"]/div)[1]').text
#     driver.find_element('xpath', '//p[text()="6"]/..').click()
#     assert wait.until(
#         expected_conditions.visibility_of_element_located(('xpath', '//span[text() = "6"]'))).is_displayed()
#
#
# @pytest.mark.usefixtures('pre_and_postcondition')
# @pytest.mark.parametrize('url', ['http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html'])
# @pytest.mark.integration
# def test_drag_and_drop(url):
#     driver.get(url)
#     for i in range(1, 8):
#         src_ele = driver.find_element('id', f'box{i}')
#         target_ele = driver.find_element('id', f'box10{i}')
#         actions.drag_and_drop(src_ele, target_ele).perform()
#
#
# @pytest.mark.usefixtures('pre_and_postcondition')
# @pytest.mark.parametrize('url', ['https://www.naukri.com/'])
# @pytest.mark.system
# def test_job_search(url):
#     driver.get(url)
#     driver.find_element('xpath', '//input[contains(@placeholder ,"Enter skills")]').send_keys('Automation Testing')
#     driver.find_element('id', 'expereinceDD').click()
#     driver.find_element('xpath', '//div/following::li//span[text() = "Fresher"]').click()
#     driver.find_element('xpath', '//input[@placeholder = "Enter location"]').send_keys('Hosur')
#     driver.find_element('xpath', '//div[text() = "Search"]').click()

# Functional:
# collected 4 items / 3 deselected / 1 selected
# test_pymarkers.py::test_fb_login[https://www.facebook.com-surya123@gmail.com-Surya@123]
# DevTools listening on ws://127.0.0.1:56439/devtools/browser/e820cb48-9063-4288-bc55-4fb3d854fe27
# PASSED                                                               [100%]
# ==================== 1 passed, 3 deselected in 29.98s ========================

# Integration:
# collected 4 items / 2 deselected / 2 selected
#
# test_pymarkers.py::test_select_date[https://www.makemytrip.com/]
# DevTools listening on ws://127.0.0.1:56592/devtools/browser/f5dbe935-4b25-4b37-8701-c117ec6fa435
# PASSED                                                            [ 50%]
# test_pymarkers.py::test_drag_and_drop[http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html]
# DevTools listening on ws://127.0.0.1:56634/devtools/browser/84b4e860-d009-4656-a961-c4bbc1c20490
# PASSED                                                            [100%]
# ============= 2 passed, 2 deselected in 47.90s =====================

# System:
# collected 4 items / 3 deselected / 1 selected
# test_pymarkers.py::test_job_search[https://www.naukri.com/]
# DevTools listening on ws://127.0.0.1:56554/devtools/browser/10e6ac99-9978-4437-844a-35da8d4828eb
# PASSED                                                            [100%]
# ============= 1 passed, 3 deselected in 21.69s ==========================
"""
