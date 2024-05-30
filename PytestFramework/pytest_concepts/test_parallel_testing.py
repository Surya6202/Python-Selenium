# """
# Parallel Execution:
# It's a process where multiple tests are executed simultaneously/in parallel in different thread processes.
# With respect to Selenium and pytest, it allows you to execute multiple tests on different browsers, devices,
# environments in parallel and at the same time, instead of running it sequentially.
# The main purpose of running tests in parallel mode is to reduce execution time and do maximum environment
# coverage (browsers/devices/environment) in less time.
# By default, pytest runs tests in sequential order.
# In a real scenario, a test suite will have a number of test files and each file will have a bunch of tests.
# This will lead to a large execution time.
# To overcome this, pytest provides us with an option to run tests in parallel.
# For parallel excution we need to install a plugin called 'pytest-xdist ' with help of pip.

# Installation steps:
# Launch the command prompt
# Enter 'pip install pytest-xdist' and click enter button.

# Syntax:
# pytest filename.py -n (number of threads)
# pytest -n(number of threads)

# def test_zee5():
#     print('Zee5 launched')
#
#
# def test_hotstar():
#     print('Hotstar launched')
#
#
# def test_netflix():
#     print('Netflix launched')
#
#
# def test_sony_live():
#     print('Sony live launched')

# 4 workers [4 items]
# ....
# ================================================================================= 4 passed in 1.90s ==================================================================================
# PS D:\Programming\Python\PythonSelenium\pytest_framework> pytest test_parallel_testing.py -rA -n4
# =============================== test session starts ====================================
# platform win32 -- Python 3.12.0, pytest-7.4.3, pluggy-1.3.0
# rootdir: D:\Programming\Python\PythonSelenium\pytest_framework
# configfile: pytest.ini
# plugins: html-4.1.1, metadata-3.0.0, xdist-3.5.0
# 4 workers [4 items]
# ....                                                                                                                                                                            [100%]
# ======================================== PASSES ==========================================
# ______________________________________ test_zee5 _________________________________________
# [gw0] win32 -- Python 3.12.0 C:\Users\Surya R\AppData\Local\Programs\Python\Python312\python.exe
# ---------------------------------- Captured stdout call ----------------------------------
# Zee5 launched
# _____________________________________ test_hotstar ________________________________________
# [gw1] win32 -- Python 3.12.0 C:\Users\Surya R\AppData\Local\Programs\Python\Python312\python.exe
# ---------------------------------- Captured stdout call -----------------------------------
# Hotstar launched
# _____________________________________ test_sony_live _______________________________________
# [gw3] win32 -- Python 3.12.0 C:\Users\Surya R\AppData\Local\Programs\Python\Python312\python.exe
# ---------------------------------- Captured stdout call ------------------------------------
# Sony live launched
# ______________________________________ test_netflix _________________________________________
# [gw2] win32 -- Python 3.12.0 C:\Users\Surya R\AppData\Local\Programs\Python\Python312\python.exe
# ----------------------------------- Captured stdout call -------------------------------------
# Netflix launched
# ================================== short test summary info ====================================
# PASSED test_parallel_testing.py::test_zee5
# PASSED test_parallel_testing.py::test_hotstar
# PASSED test_parallel_testing.py::test_sony_live
# PASSED test_parallel_testing.py::test_netflix
# ===================================== 4 passed in 1.98s ========================================

# Scripts:

# from selenium import webdriver
# import pytest
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
#     driver.implicitly_wait(30)
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
#     actions.pause(10).click().perform()
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

# 4 workers [4 items]
# scheduling tests via LoadScheduling
# test_parallel_testing.py::test_drag_and_drop[http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html]
# test_parallel_testing.py::test_job_search[https://www.naukri.com/]
# test_parallel_testing.py::test_select_date[https://www.makemytrip.com/]
# test_parallel_testing.py::test_fb_login[https://www.facebook.com-surya123@gmail.com-Surya@123]
# [gw2] [ 25%] PASSED test_parallel_testing.py::test_drag_and_drop[http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html]
# [gw0] [ 50%] PASSED test_parallel_testing.py::test_fb_login[https://www.facebook.com-surya123@gmail.com-Surya@123]
# [gw3] [ 75%] PASSED test_parallel_testing.py::test_job_search[https://www.naukri.com/]
# [gw1] [100%] PASSED test_parallel_testing.py::test_select_date[https://www.makemytrip.com/]
# ===================== 4 passed in 62.48s (0:01:02) ===============================
# """
