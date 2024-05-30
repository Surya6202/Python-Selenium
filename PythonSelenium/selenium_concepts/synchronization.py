"""
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from utilities import chrome_options

driver = webdriver.Chrome(chrome_options)

# Synchronization:
# It plays a very vital role in automation, test-script execution and web-application loading speed need to be
# in sync to perform the operation.
# Generally the test-script execution speed is faster than the web-application loading speed.
# If the application slows down for any reasons like network, heavy load, etc..., then the code keeps on checking for
# the particular web element and,If the code doesn't able to find that element it fails, by throwing exceptions like
# NoSuchElement, etc...
# Hence, To maintain the synchronization during the automation.

# In Selenium WebDriver, Synchronization can be divided into two types:
# 1) Unconditional synchronization.
# 2) Conditional synchronization.

# 1) Unconditional synchronizatin:
# This synchronization comes from python language where we just specify the time limit that pauses the code for
# particular specified time and then it starts to execute the next line of code.
# It's also called as static wait or hard wait.
# Here no conditions are passed.
# In python there is a module for time-related operations from that we should call a function called sleep().
# The sleep() will delay the execution for a given number of seconds and the argument may be a floating point number for
# subsecond precision.
# To use this function, We should import it from time module.
# It's not advisable to use for automation as it just waits for the specified time even if it has found the web element
# or performed the required action.

# from time import sleep # Import the sleep(), from the time module
# driver.get('https://www.zee5.com/')
# sleep(3) # It'll add a delay of given seconds after that it'll start to execute further lines.

# 2) Conditional synchronization:
# In this synchronization, Conditions will be set along with the timeout limit.
# Code will wait for the specified time declared until the expected condition gets satisfied, then it executes
# the next line of code.
# It is divided into three types:
# * Pageload timeout.
# * Implicit wait.
# * Explicit wait.

# 1) Pageload timeout:
# It's the amount of time given to load the webpage in the browser which has happened in the current session.
# get() has infinite waiting capacity to get loaded the webpage.
# If the given time is not sufficient to load the webpage, the webpage loading process will be freezed.
# It'll throw 'TimeoutException' with the appropriate time needed to load the webpage as a error message.
# The error message is 'TimeoutException: Message: timeout: Timed out receiving message from renderer: 1.568'.

# try:
#     driver.set_page_load_timeout(5)
#     driver.get('https://www.zee5.com/')
# except TimeoutException:
#     print('Time is insufficient for webpage to get loaded')
# finally:
#     print('TimeoutException')

# To avoid this exception, We need to specify certain amount of time in seconds.

# try:
#     driver.set_page_load_timeout(10)
#     driver.get('https://www.zee5.com/')
# except TimeoutException:
#     print('Time is insufficient for webpage to get loaded.')
# finally:
#     print('Time is sufficient for webpage to get loaded.')

# 2) Implicit wait:
# It's one of the popular wait in selenium webdriver that helps us to save the time while waiting for the webelements to
# get loaded on the webpage.
# Here we provide the time to fetch the webelements.
# It uses 500 milliseconds of polling period.
# If the webelements found anytime within the specified time then the code does not wait for the remaining duration as
# it auto-nullifies the remaining time.
# If the webelement is not found within the time, it'll throw 'NoSuchElementException'.
# It waits for an element to be found, or a command to complete.
# It's enough to declare this method one time per session/ script.
# We've to pass the number of seconds as an argument in the form int and float(for sub precision).
# Implicit wait is also called as global wait/ intelligent wait and it has a drawback that if the locator value
# is incorrect, it'll wait until the specified time.

# driver.get('https://omayo.blogspot.com/')
# driver.find_element('class name', 'dropbtn').click()
# try:
#     driver.find_element('link text', 'Facebook').click()
# except NoSuchElementException:
#     print('Time is insufficient to element get loaded!')
# finally:
#     print('NoSuchElementException')

# The above script will throw an exception as it couldn't click the option immediately as that element required some
# time to be visible so we should give implicit wait for it.

# driver.get('https://omayo.blogspot.com/')
# driver.implicitly_wait(30)
# driver.find_element('class name', 'dropbtn').click()
# driver.find_element('link text', 'Facebook').click()

# using implicit wait also has certain drawback as it's a global wait it'll provide time to all the elements to
# get loaded suppose if the locator value is incorrect, it'll wait untill the specified time.
# The below script is an example for this drawback

# driver.get('https://omayo.blogspot.com/')
# driver.implicitly_wait(20)
# driver.find_element('class name', 'dropbtn').click()
# try:
#     driver.find_element('link text', 'Facebook123').click()
# except NoSuchElementException:
#     print('Element is not in DOM, provided incorrect locator!')
# finally:
#     print('NoSuchElementException')

# So to overcome this drawback, We should go for explicit wait where we specify the time only for certain elements or
# certain operation to be performed.

# 3) Explicit wait:
# It's also a popular wait in selenium webdriver that tells webdriver to wait for certain expected conditions like
# * expected title of the webpage to be loaded.
# * expected element of the webpage to be loaded and visible.
# * expected element to be clickable.
# * wait until all the elements get loaded in the DOM etc...
# Here we provide certain time to fulfil that conditions.
# This wait is also called as local wait/ smart wait, used for only particular command or for particular webelement.
# If the condition is satisfied the driver will start to execute next line of the code.
# If the given condition is not satisfied within the specified time, then we'll get 'TimeoutException'.
# Also sometimes it's called as smart waits because they don’t wait out the entire duration defined in the code.
# Instead, the test continues to execute as soon as the element is detected or the command get satisfied.
# Explicit wait is classified into two types:
# * Normal wait/ webdriver wait.
# * Advanced wait/ fluent wait.

# Steps to apply explicit wait in test-script:
# 1) Create an instance of webdriverwait class which is an inbuilt class in selenium which is a concrete class and
# accepts four arguments:
# * webdriver reference.
# * timeout in seconds.
# * polling frequency.
# * Ignored exceptions.
# 2) Upon webdriverwait reference we should call the until().
# 3) We've to pass the module 'expected_conditions' as an argument for until method and this a module from selenium
# package which is having many inbuilt functions.
# Depending upon the conditions, we should use the required function.

# WebDriverWait constructor arguments:
# driver - Instance of WebDriver (Ie, Firefox, Chrome or Remote).
# timeout - Number of seconds before timing out
# poll frequency - sleep interval between calls and by default, it is 0.5 second.
# ignored exceptions - iterable structure of exception classes ignored during calls and by default, it
# contains NoSuchElementException only.

# Note: It's not mandatory to give poll-frequency and ignored exceptions, it's not used in real-time.

# 3.1) Webdriver wait:
# Here, the Webdriver is directed to wait until a certain condition occurs before proceeding with executing the code.
# Setting Explicit Wait is important in cases where there are certain elements that naturally take more time to load.
# If one sets an implicit wait command, then the browser will wait for the same time frame before
# loading every web element. This causes an unnecessary delay in executing the test script.
# Explicit wait is more intelligent, but can only be applied for specified elements.
# However, it is an improvement on implicit wait since it allows the program to pause for dynamically loaded
# 'Ajax elements' and we can habdle it as Webpages make ajax calls, to retrieve small amount of data from server without
# the need for reloading the webpage.
# To declare explicit wait, one has to use 'Expected Conditions'.

# driver.get('https://omayo.blogspot.com/')
# wait = WebDriverWait(driver=driver, timeout=20)
# driver.find_element('class name', 'dropbtn').click()
# try:
#     wait.until(expected_conditions.visibility_of_element_located(('link text', 'Facebook12'))).click()
# except TimeoutException:
#     print('Element is not in DOM, provided incorrect locator!')
# finally:
#     print('TimeoutException')

# If the time is not sufficient for that operation, it'll throw 'TimeoutException'.

# driver.get('https://omayo.blogspot.com/')
# wait = WebDriverWait(driver=driver, timeout=20)
# driver.find_element('class name', 'dropbtn').click()
# try:
#     wait.until(expected_conditions.visibility_of_element_located(('link text', 'Facebook'))).click()
# except TimeoutException:
#     print('Element is not in DOM, provided incorrect locator!')
# finally:
#     print('Time is sufficient for that element!')

# 3.2) Fluent wait:
# It's similar to webdriver wait where driver will wait for specified to perform the condition in addition to it we can
# set the frequency intervals and we can ignore some exceptions not all.
# This wait is most useful when interacting with web elements that can take longer durations to load that often
# occurs in Ajax applications.
# It is possible to set a default polling period as needed and we can configure the wait to ignore any exceptions during
# the polling period.

# driver.get('https://omayo.blogspot.com/')
# wait = WebDriverWait(driver=driver, timeout=20, poll_frequency=2, ignored_exceptions=[NoSuchElementException])
# driver.find_element('class name', 'dropbtn').click()
# wait.until(expected_conditions.visibility_of_element_located(('link text', 'Facebook'))).click()

# Advantages of Explicit wait:
# * With explicit waits, more expected success conditions can be implemented.
# * It allows the coder to wait for the presence or absence of elements/conditions.
# * The timeout can be customized on every call.

# Expected conditions:
# It's provided by Selenium WebDriver are used for performing Explicit Waits on a certain condition.
# The Selenium WebDriver waits for the specified condition to occur before it can proceed further with the execution.
# This provides the required wait time between the actions that have to be performed.

# wait = WebDriverWait(driver, 20, 2)

# Expected condition functions:
# 1) alert_is_present():
# This function will check whether the current session has any alert popup.
# If it encounters any alert popup, we handle the popup by its methods.
# If any alerts are not displayed, we'll get 'TimeoutException'.
# The return type of this function is Alert upon that we can perform the Alert methods.

# driver.get('https://omayo.blogspot.com/')
# wait = WebDriverWait(driver, 20, 2)
# driver.find_element('id', 'alert1').click()
# wait.until(expected_conditions.alert_is_present()).accept()

# 2) visibility_of_element_located():
# This function will check whether the element is present in DOM and also visible in the webpage.
# Also it verifies the rect of the element that is greater than 0.
# We've to pass the locator and locator value in the form of tuple as an argument.
# The return type of this function is webelement upon that we can perform the webelement methods.

# driver.get('https://omayo.blogspot.com/')
# wait = WebDriverWait(driver, 20, 2)
# Element is visibe:
# driver.find_element('class name', 'dropbtn').click()
# wait.until(expected_conditions.visibility_of_element_located(('link text', 'Flipkart'))).click()

# Element is invisible:
# try:
#     wait.until(expected_conditions.visibility_of_element_located(('id', 'hbutton')))
# except TimeoutException:
#     print('Element is invisible in the webpage.')

# 3) element_to_be_clickable():
# This function will check whether the element is visible and enabled so that we can click it.
# We've to pass the webelement or tuple of locator and its value as an argument.
# The return type of this function is webelement upon that we can perform the webelement methods.

# driver.get('https://omayo.blogspot.com/')
# wait = WebDriverWait(driver, 20, 2)

# Element is clickable:
# wait.until(expected_conditions.element_to_be_clickable(('id', 'but2'))).click()

# Element is unclickable:
# try:
#     wait.until(expected_conditions.element_to_be_clickable(('id', 'but1'))).click()
# except TimeoutException:
#     print('Element is disabled in the webpage.')

# 4) element_to_be_selected():
# This function will check whether specified checkbox/ radio-button element is selected or not in te page.
# If the webelement is selected, it'll return true.
# If not we'll get 'TimeoutException'.
# The return type of this function is boolean.

# driver.get('https://omayo.blogspot.com/')
# wait = WebDriverWait(driver, 20, 2)
# # Element is selected:
# checkbox = driver.find_element('xpath', '(//input[@name = "accessories"])[2]')
# wait.until(expected_conditions.element_to_be_selected(checkbox))
# print('Element is selected in the webpage.')

# Element is not selected:
# checkbox = driver.find_element('xpath', '(//input[@name = "accessories"])[3]')
# try:
#     wait.until(expected_conditions.element_to_be_selected(checkbox))
# except TimeoutException:
#     print('Element is not selected in the webpage.')

# 5) presence_of_element_located():
# This function will check whether the element is present in the DOM or not.
# If the element is present, we can perform the required webelement action.
# If not we'll get 'TimeoutException'.
# The return type of this function is webelement upon that we can perform the webelement methods.
# We've to pass tuple of locator and its value as an argument.

# driver.get('https://omayo.blogspot.com/')
# wait = WebDriverWait(driver, 20, 2)
# Element is present:
# wait.until(expected_conditions.presence_of_element_located(('id', 'hbutton')))
# print('Element is present in the DOM.')

# Element is not present:
# try:
#     wait.until(expected_conditions.presence_of_element_located(('id', 'hbut2'))).click()
# except TimeoutException:
#     print('Element is not present in the DOM.')

# 6) invisibility_of_element() and invisibility_of_element_located():
# This functions are similar to each other and are used to check whether the element is invisible or not present
# in the DOM.
# The return type of this function is webelement or boolean upon that we can perform the webelement methods.
# We to pass the tuple of locator and its value as an argument.

# driver.get('https://the-internet.herokuapp.com/dynamic_loading/1')
# wait = WebDriverWait(driver, 20, 2)
# driver.find_element('tag name', 'Button').click()

# assert wait.until(expected_conditions.invisibility_of_element(('id', 'loading')))
# text = driver.find_element('xpath', '//div[@id = "finish"]/h4').text
# print(text)

# wait.until(expected_conditions.invisibility_of_element_located(('id', 'loading')))
# text = driver.find_element('xpath', '//div[@id = "finish"]/h4').text
# print(text)


# 7) url_matches() and url_to_be():
# This functions are similar to each other and are used to check whether the current/ actual url pattern
# is exactly matching to the expected url pattern.
# If it matches it'll return true orelse we'll get 'TimeoutException.
# We've to pass the url pattern in the form of string as an argument.
# The return type of this function is boolean.

# driver.get('https://www.zee5.com/')
# wait = WebDriverWait(driver, 20, 2)
# expected_url = 'https://www.zee5.com/'

# assert wait.until(expected_conditions.url_matches(expected_url))
# print('The actual url pattern is matching to the expected url pattern')

# assert wait.until(expected_conditions.url_to_be(expected_url))
# print('The actual url pattern is matching to the expected url pattern')

# 8) url_contains() and url_changes():
# This functions are similar to each where it will check actual url of the page contains the expected
# url substring or the url is quite matching to the expected url.
# If it matches it'll return true orelse we'll get 'TimeoutException.
# We've to pass the url pattern in the form of string as an argument.
# The return type of this function is boolean

# driver.get('https://www.zee5.com/')
# wait = WebDriverWait(driver, 20)
# expected_url = 'zee5'

# assert wait.until(expected_conditions.url_contains(expected_url))
# print('The actual url of the page contains the expected url substring.')

# assert wait.until(expected_conditions.url_changes(expected_url))
# print('The actual url of the page contains the expected url substring.')

# 9) title_is():
# This function is used to check whether the current/ actual title of the page is exactly matching to the expected title.
# If it matches it'll return true orelse we'll get 'TimeoutException.
# We've to pass the url pattern in the form of string as an argument.
# The return type of this function is boolean

# driver.get('https://en.wikipedia.org/wiki/Family_Guy')
# wait = WebDriverWait(driver, 20)
# expected_title = 'Family Guy - Wikipedia'
# assert wait.until(expected_conditions.title_is(expected_title))
# print('The actual title is exactly matching to the expected title')

# 10) title_contains():
# This function is similar to the title_is() where it will check actual title of the page contains the expected
# title substring.
# If it matches it'll return true orelse we'll get 'TimeoutException.
# We've to pass the url pattern in the form of string as an argument.
# The return type of this function is boolean

# driver.get('https://en.wikipedia.org/wiki/Family_Guy')
# wait = WebDriverWait(driver, 20)
# expected_title = 'Family Guy'
# assert wait.until(expected_conditions.title_contains(expected_title))
# print('The actual title of the page contains the expected title substring.')

# 11) presence_of_all_elements_located():
# This function is used to check whether the webpage has atleast one weblement.
# We've to pass the tuple of locator and its value as an argument.
# The return type of this function is list of webelement upon that we can perform the webelement methods.

# driver.get('https://www.instagram.com/')
# wait = WebDriverWait(driver, 20)
# buttons = wait.until(expected_conditions.presence_of_all_elements_located(('tag name', 'Button')))
# buttons[0].submit()

# 12) visibility_of_all_elements_located():
# This function will check whether the element is present in DOM and also visible in the webpage.
# Also it verifies the rect of the element that is greater than 0.
# We've to pass the locator and locator value in the form of tuple as an argument.
# The return type of this function is list of webelement upon that we can perform the webelement methods.

# driver.get('https://www.instagram.com/')
# wait = WebDriverWait(driver, 20)
# text_fields = wait.until(expected_conditions.visibility_of_all_elements_located(('tag name', 'input')))
# text_fields[0].send_keys('Surya')

# 13) text_to_be_present_in_element_attribute():
# This function is used to check whether the actual text of the attribute value of the elements is matching to the
# expected text.
# If it matches it'll return true orelse we'll get 'TimeoutException'.
# The return type of this function is boolean.

# driver.get('https://www.facebook.com/')
# wait = WebDriverWait(driver, 20)
# expected_text = 'Email address or phone number'
# assert wait.until(expected_conditions.text_to_be_present_in_element_attribute
#            (('id', 'email'), 'placeholder', expected_text))
# print('The actual attribute value text of the element is matching to the expected text.')

# 14) text_to_be_present_in_element():
# This function is used to check whether the actual text of the element is matching to the expected text.
# If it matches it'll return true orelse we'll get 'TimeoutException'.
# The return type of this function is boolean.

# driver.get('https://www.facebook.com/')
# wait = WebDriverWait(driver, 20)
# expected_text = 'Forgotten password?'
# assert wait.until(expected_conditions.text_to_be_present_in_element
#                   (('link text', 'Forgotten password?'), expected_text))
# print('The actual text of the element is matching to the expected text.')

# 15) text_to_be_present_in_element_value():
# This function is used to check whether the actual value of the element is matchibg to the expected text.
# If it matches it'll return true orelse we'll get 'TimeoutException'.
# The return type of this function is boolean.

# driver.get('https://www.facebook.com/')
# wait = WebDriverWait(driver, 20)
# expected_text = ''
# assert wait.until(expected_conditions.text_to_be_present_in_element_value
#                   (('id', 'email'), expected_text))
# print('The actual value of the element is matching to the expected text')

driver.quit()
"""
