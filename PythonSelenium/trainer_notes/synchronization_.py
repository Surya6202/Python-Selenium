'''
Synchronization : Matching the speed of the webdriver to that of webapplication

unconditional synchronization : No conditions passed. Here we delay the execution by giving sleep()
time.sleep(seconds)

conditional synchronization : Conditions are taken
    i) implicit wait : Conditions will be taken internally automatically.
                        If the element is located within less than the given seconds, it'll execute right away. It will completely wait for entire time.
                        It can be applied for find_element/find_elements method
                        One implicit wait is enough for the whole program

    ii) explicit wait --> Also called as WebDriverWait. Here we will be passing the conditions explicitly.

'''
import time

#---------------------------------------------------------------
## unconditional synchronization
# import time
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=opts)
#
# driver.get(r'C:\Users\Ramya\PycharmProjects\selenium_QCO_SOFPSD_E3\files\loading.html')
# time.sleep(20)      ## here the driver will not check whether the next element is present or not. It will just wait for 20 seconds
#
# driver.find_element('xpath', '//input[@name="fname"]').send_keys('Ram')
# time.sleep(2)
# driver.find_element('xpath', '//input[@name="lname"]').send_keys('Sharma')

#--------------------------------------------------------------------
## implicit_wait

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=opts)
#
# driver.get(r'C:\Users\Ramya\PycharmProjects\selenium_QCO_SOFPSD_E3\files\loading.html')
# driver.implicitly_wait(30)
#
# driver.find_element('xpath', '//input[@name="fname"]').send_keys('Ram')
# driver.find_element('xpath', '//input[@name="lname"]').send_keys('Sharma')

#-------------------------------------------------------------------------
# ## explicit_wait
#
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=opts)
#
# wait_obj = WebDriverWait(driver, 30)
#
# driver.get(r'C:\Users\Ramya\PycharmProjects\selenium_QCO_SOFPSD_E3\files\loading.html')
# time.sleep(2)
#
# element = driver.find_element('xpath', '//div[contains(text(), "FirstName: ")]')
# wait_obj.until(expected_conditions.visibility_of(element))
#
# driver.find_element('xpath', '//input[@name="fname"]').send_keys('John')

#-----------------------------------------------------------------------
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=opts)

wait_obj = WebDriverWait(driver, 30)

driver.get('https://www.saucedemo.com/')
time.sleep(2)
driver.implicitly_wait(30)

driver.find_element('id', 'user-name').send_keys('standard_user')
time.sleep(2)
driver.find_element('id', 'password').send_keys('secret_sauce')
time.sleep(2)
driver.find_element('id', 'login-button').click()

backpack = driver.find_element('xpath', '//div[text()="Sauce Labs Backpack"]')

wait_obj.until(expected_conditions.visibility_of(backpack))
driver.find_element('xpath', '(//button[text()="Add to cart"])[1]').click()

#-----------------------------------------------------------------
# ## progress bar example
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=opts)
#
# driver.get(r'C:\Users\Ramya\PycharmProjects\selenium_QCO_SOFPSD_E3\files\progressbar.html')
# time.sleep(2)
#
# wait_obj = WebDriverWait(driver, 45)
#
# driver.find_element('xpath', '//button[text()="Click Me"]').click()
# wait_obj.until(expected_conditions.presence_of_element_located(('xpath', '//div[text()="100%"]')))
# time.sleep(1)
#
# driver.find_element('xpath', '//button[text()="Click Me"]').click()
























