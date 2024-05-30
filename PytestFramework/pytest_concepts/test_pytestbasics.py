"""
# Pytest:
# It's a testing framework that allows users to write test codes using Python programming language.
# It's free and open-source testing framework which can be used by both developers and test engineers.
# It helps you to write simple and scalable test cases for databases, APIs and UI.
# Test engineers mainly use it for automation testing.
# It supports unit testing, functional testing, and API testing.

# Note:
# Developers use pytest for unit testing of the source code.
# Automation test engineers use pytest for developing the test scripts in a more optimized way.

# prerequisites for pytest framework:
# We should install the python version 3.5 or above.

# Advantages of pytest:
# * It's free and open-source framework.
# * Because of its simple syntax, pytest is very easy to use.
# * It allows us to skip a subset of the tests during execution.
# * It allows us to run a subset of the entire test suite.
# * We can group the test cases and generate xml reports.
# * It can run multiple tests in parallel, which reduces the execution time of the test suite.
# * It has its own way to detect the test file and test functions automatically, if not mentioned explicitly.
# * Provides a compact and simple test suite.
# * Highly extensible with many plugins available, such as the Pytest HTML plugin, which can be added to your project
# to print HTML reports with a single command-line option.
# * It has large community support.
# * It helps to cover all parameter combinations without rewriting test cases.

# Disadvantages:
# * Its proprietary routines prevent compatibility.
# * Limited official documentation.
# * Additional setup and configuration is required for it to integrate with other frameworks.
# * Debugging issues related to fixtures setup and teardown can sometimes be hard in complex scenarios.
# * Extensive plugins might be overwhelming.

# Pytest installation:
# We've to install it by using a pip command.
# 1) launch the command prompt.
# 2) Enter the command: 'pip install pytest'
# 3) Check whether it's installed or not by entering another command 'pip show pytest'/ 'pytest --version' and
# if we get the version, the pytest is installed correctly.
# 4) To know more commands related to pytest, enter 'pytest -h'/ 'pytest --help'.

# Rules:
# 1) Pytest will automatically detect the files from current and sub directories and packages so the files, class,
# methods and functions name should be prefixed with 'test'.
# 2) Then only the pytest will collect and execute it.
# 3) If their names is not prefixed with test, pytest can't recognize it and it won't collect any files for execution.
# 4). Filename (module) should always start with 'test_filename'/ 'testfilename'.
#         Eg : test_filename.py
# 5). Classname should always start with 'test_classname'/ 'testclassname'.
#         Eg : class TestClassname
# 6). Function name should always start with 'test_function_name'/ 'testfunctionname'.
#         Eg : def test_functionname():

# Note:
# We should follow these conventions because, pytest will automatically recognize the files starting with test_,
# automatically recognizes the classes starting with Test, automatically recognizes the functions starting with test_

# Pytest execution:
# To execute a file, click on terminal and enter pytest filename.py and click on enter button.
# To execute all files, click on terminal and enter pytest and click on enter button.

# Pytest exit codes:
# 1) Exit code 0 - All tests were collected and passed successfully.
# 2) Exit code 1 - Tests were collected and run but some tests failed.
# 3) Exit code 2 - the user interrupted Test execution.
# 4) Exit code 3 - Internal error happened while executing tests.
# 5) Exit code 4 - pytest command line usage error.
# 6) Exit code 5 - No tests were collected.

# import pytest
# from selenium import webdriver
#
# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)
# options.add_argument('--start-maximized')
#
# driver = webdriver.Chrome(options=options)
# driver.implicitly_wait(20)

# def test_register():
#     print('Account registered successfully!')
#
#
# def login():
#     print('Logged in successfully!')

# ============================= test session starts =============================
# collecting ... collected 1 item
# test_pytestbasics.py::test_register PASSED                               [100%]Account registered successfully!
# ============================== 1 passed in 0.40s ==============================
# Process finished with exit code 0

# Here login function is ignored as it doesn't follow pytest convention.

# def test_register():
#     print('Account registered successfully!')
#
#
# def test_login():
#     print('Logged in successfully!')
#
#
# def test_search_product():
#     print('Product is found.')
# ============================= test session starts =============================
# collecting ... collected 3 items
# test_pytestbasics.py::test_register PASSED                               [ 33%]Account registered successfully!
# test_pytestbasics.py::test_login PASSED                                  [ 66%]Logged in successfully!
# test_pytestbasics.py::test_search_product PASSED                         [100%]Product is found.
# ============================== 3 passed in 0.03s ==============================
# Process finished with exit code 0

# Pytest_assertions:

# def test_add():
#     a, b = 1, 2
#     assert a + b == b
#
#
# def test_sub():
#     a, b = 1, 2
#     assert a - b == a
#
#
# def test_mul():
#     a, b = 1, 2
#     assert a * b == b


# ============================= test session starts =============================
# collecting ... collected 3 items
# test_pytestbasics.py::test_add FAILED                                    [ 33%]
# test_pytestbasics.py:101: AssertionError
# test_pytestbasics.py::test_sub FAILED                                    [ 66%]
# test_pytestbasics.py:106: AssertionError
# test_pytestbasics.py::test_mul PASSED                                    [100%]
# ========================= 2 failed, 1 passed in 0.16s =========================
# Process finished with exit code 1

# def test_add():
#     sleep(5)
#     a, b = 1, 2
#     assert a + b == b

# ============================= test session starts =============================
# collecting ... collected 1 item
# test_pytestbasics.py::test_add
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!! KeyboardInterrupt !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# D:\Programming\Python\PythonSelenium\pytest_framework\test_pytestbasics.py:102: KeyboardInterrupt
# (to show a full traceback on KeyboardInterrupt use --full-trace)
# ============================ no tests ran in 0.74s ============================
# Test ignored.
# Process finished with exit code 2

# @pytest.mark.xfail(reason = 'Intention error', raises = 'NoSuchElementException')
# def test_heroine():
#     assert False
# ============================= test session starts =============================
# collecting ... collected 1 item
# INTERNALERROR> TypeError: isinstance() arg 2 must be a type, a tuple of types, or a union
# ============================== 1 passed in 0.41s ==============================
# Test ignored.
# Process finished with exit code 3

# def register():
#     print('Account registered successfully!')
# ============================= test session starts =============================
# collecting ... collected 0 items
# ============================ no tests ran in 0.01s ============================
# Process finished with exit code 5
# Empty suite (If we dont follow the conventions, pytest won't execute it.)

# Selenium-script:
# def test_navigate_to_url():
#     driver.get('Https://www.facebook.com/')
#
#
# def test_enter_details():
#     driver.find_element('id', 'email').send_keys('surya123@gmail.com')
#     sleep(2)
#     driver.find_element('id', 'pass').send_keys('Surya@123')
#
#
# def test_submit():
#     sleep(2)
#     driver.find_element('name', 'login').submit()
#
#
# def test_teardown():
#     driver.minimize_window()
#     driver.quit()

# ============================= test session starts =============================
# collecting ... collected 4 items
# test_pytestbasics.py::test_navigate_to_url PASSED                        [ 25%]
# test_pytestbasics.py::test_enter_details PASSED                          [ 50%]
# test_pytestbasics.py::test_submit PASSED                                 [ 75%]
# test_pytestbasics.py::test_teardown PASSED                               [100%]
# ============================= 4 passed in 38.76s ==============================
# Process finished with exit code 0

# def test_login():
#     print('Logged in.')
#
#
# def test_search_product():
#     print('product is found.')
#
#
# def test_add_product():
#     print('product added.')
#
#
# def test_logout():
#     print('logged out.')

# Command-line terminal execution:
# 1) enter 'pytest' (entire test execution)
# collected 4 items
# test_pytestbasics.py ....                    [100%]
# ============================== 4 passed in 0.34s ==========================================
# This command will detect all the tests and executes it.

# 2) enter 'pytest test_pytestbasics.py' (specified file test execution)
# collected 4 items
# test_pytestbasics.py ....                    [100%]
# ============================== 4 passed in 0.29s ==========================================
# This command will detect all the test in the specified file and executes it.

# 3) enter 'pytest test_pytestbasics.py -v' (Verbosity/ Verbose - to get detailed explanation of the test execution.)
# collected 4 items
# test_pytestbasics.py::test_login PASSED                   [ 25%]
# test_pytestbasics.py::test_search_product PASSED          [ 50%]
# test_pytestbasics.py::test_add_product PASSED             [ 75%]
# test_pytestbasics.py::test_logout PASSED                  [100%]
# =================================== 4 passed in 0.29s ========================================

# 4) enter 'pytest test_pytestbasics.py -s' (scripting - This will print all the printing statements)
# collected 4 items
# test_pytestbasics.py Logged in.
# .product is found.
# .product added.
# .logged out.
# ==================================== 4 passed in 0.32s =========================================

# 5) enter 'pytest -h' (help - gets information about all the options of pytest)

# 5) enter 'pytest test_pytestbasics.py -q' (quiet - This will give a short summary of the test execution)
# 4 passed in 0.29s

# 6) enter 'pytest test_pytestbasics.py -rA' (This will give complete detailed summary of the test execution)
# collected 4 items
# test_pytestbasics.py ....                                              [100%]
# ==================================== PASSES ===========================================
# __________________________________ test_login _________________________________________
# ----------------------------- Captured stdout call ------------------------------------
# Logged in.
# ______________________________ test_search_product _____________________________________
# ------------------------------ Captured stdout call ------------------------------------
# product is found.
# ________________________________ test_add_product ______________________________________
# ------------------------------ Captured stdout call ------------------------------------
# product added.
# __________________________________ test_logout _________________________________________
# ------------------------------ Captured stdout call ------------------------------------
# logged out.
# ============================= short test summary info ===================================
# PASSED test_pytestbasics.py::test_login
# PASSED test_pytestbasics.py::test_search_product
# PASSED test_pytestbasics.py::test_add_product
# PASSED test_pytestbasics.py::test_logout
# ================================= 4 passed in 0.29s ======================================

# 7) enter 'pytest test_filename.py -k' (keyword - It's used to execute particular test by specifying the
# keyword of that test function or even we can exculde it from the execution and its done with logical expression)
# collected 4 items / 3 deselected / 1 selected
# test_pytestbasics.py .                      [100%]
# ==================== 1 passed, 3 deselected in 0.03s =========================

# 8) enter 'pytest test_filename.py --junit-xml="filepath/filename.xml"' (used to generate xml report and save it in the
# specified location.)
# collected 4 items
# test_pytestbasics.py ....                    [100%]
# ----- generated xml file: D:\Programming\Python\PythonSelenium\pytest_framework\files\junit_report.xml -----
# ==================== 4 passed in 0.31s =========================

# 9) enter 'pytest test_filename.py --html="filepath/filename.html"' (used to generate html report and save it in the
# specified location.)
# collected 4 items
# test_pytestbasics.py ....                    [100%]
# ----- generated html file: D:\Programming\Python\PythonSelenium\pytest_framework\files\html_report.html -----
# ==================== 4 passed in 0.31s =========================

# def test_punch_in():
#     print('Punched in at 9:00AM')
#
#
# def test_lunch_break():
#     print('Lunch break at 1:00PM')
#
#
# def test_break():
#     print('Break at 4:30 PM')
#
#
# def test_punch_out():
#     print('punched out at 6:00PM')

# Enter 'pytest test_pytestbasics.py -v -s -k in' '
# collected 4 items / 3 deselected / 1 selected
# test_pytestbasics.py::test_punch_in Punched in at 9:00AM
# PASSED
# =================== 1 passed, 3 deselected in 0.03s ===============================

# Enter 'pytest test_pytestbasics.py -v -s -k 'out or break' '
# collected 4 items / 1 deselected / 3 selected
# test_pytestbasics.py::test_lunch_break Lunch break at 1:00PM
# PASSED
# test_pytestbasics.py::test_break Break at 4:30 PM
# PASSED
# test_pytestbasics.py::test_punch_out punched out at 6:00PM
# PASSED
# ========================= 3 passed, 1 deselected in 0.04s ===============================

# Enter 'pytest test_pytestbasics.py -v -s -k punch' '
# collected 4 items / 2 deselected / 2 selected
# test_pytestbasics.py::test_punch_in Punched in at 9:00AM
# PASSED
# test_pytestbasics.py::test_punch_out punched out at 6:00PM
# PASSED
# ================== 2 passed, 2 deselected in 0.10s ========================


# class TestCalculator:
#     a = 10
#     b = 20
#
#     def test_add(self):
#         print(self.a + self.b)
#
#     def test_sub(self):
#         print(self.a - self.b)

# We can't create object for test classes and we cannot define constructor also, if try we'll get error.

# def test_navigate_to_url():
#     driver.get('https://www.saucedemo.com')
#
#
# def test_enter_credentials():
#     driver.find_element('id', 'user-name').send_keys('standard_user')
#     driver.find_element('id', 'password').send_keys('secret_sauce')
#
#
# def test_submit():
#     driver.find_element('id', 'login-button').submit()
#
#
# def test_logout():
#     sleep(2)
#     driver.find_element('xpath', '//button[text()="Open Menu"]').click()
#     sleep(3)
#     driver.find_element('xpath', '//a[text()="Logout"]').click()
#
#
# def test_teardown():
#     sleep(3)
#     driver.minimize_window()
#     driver.quit()
"""
