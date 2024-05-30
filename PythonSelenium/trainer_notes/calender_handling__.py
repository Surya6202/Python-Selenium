# import time
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=opts)
#
# driver.get('https://www.goibibo.com/')
# time.sleep(3)
#
# driver.find_element('xpath', '//span[@role="presentation"]').click()
# time.sleep(2)
#
# driver.find_element('xpath', '//span[text()="Departure"]').click()
# time.sleep(2)
#
# current_month = driver.find_element('xpath', '//div[@class="DayPicker-Caption"]')
# print(current_month.text)       ## December 2023
#
# while not current_month.text=="July 2024":
#     driver.find_element('xpath', '//span[@aria-label="Next Month"]').click()
#     current_month = driver.find_element('xpath', '//div[@class="DayPicker-Caption"]')
#
# driver.find_element('xpath', '//p[text()="12"]').click()
# time.sleep(2)
#
# driver.find_element('xpath', '//span[text()="Done"]').click()

#-------------------------------------------------------------------
## ASSIGNMENT
## 1. Go to https://testautomationpractice.blogspot.com/ and select date
## 2. Go to https://www.makemytrip.com/, select the departure date and return date
## 3. Go to https://in.hotels.com/, select the date for May 15
## 4. Go to https://www.irctc.co.in/, select the train date for March 10

#-------------------------------------------------------------------
# import time
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=opts)
#
# driver.get('https://in.hotels.com/')
# time.sleep(3)
#
# driver.find_element('xpath', '//button[@name="EGDSDateRange-date-selector-trigger"]').click()
# time.sleep(2)
#
# current_month = driver.find_element('xpath', '//span[@class="uitk-align-center uitk-month-label"]')
# print(current_month.text)
#
# while not current_month.text=='March 2024':
#     driver.find_element('xpath', '//button[@data-stid="uitk-calendar-navigation-controls-next-button"]').click()
#     current_month = driver.find_element('xpath', '//span[@class="uitk-align-center uitk-month-label"]')
#
#
# driver.find_element('xpath', '//div[text()="8"]').click()
# time.sleep(1)
#
# driver.find_element('xpath', '//button[text()="Done"]')















