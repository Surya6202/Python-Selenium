"""
from datetime import datetime
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.select import Select

from utilities import chrome_options

driver = webdriver.Chrome(chrome_options)
driver.implicitly_wait(20)
actions = ActionChains(driver)

# Calendar:
# Datepicker is the UI element that is used to generate a Calendar in web applications.
# Essential functions in a calendar require selecting a date or date range.
# Among different UI elements, the Date is essential for certain websites.
# Datepickers are often included as UI elements to websites in which the user has to select a date as an input value.
# This makes it an important feature that needs to be tested for accurate functioning using Selenium.

# Calendar type 1:
# In this calendar, We can select the date from past, present and future.
# We've to click next option multiple times to change the year.
# In this calendar type, Only present month dates are displayed.
# The dates of past and future month are not displayed.

# Future date:
# driver.get('https://seleniumpractise.blogspot.com/2016/08/how-to-handle-calendar-in-selenium.html')
# driver.find_element('id', 'datepicker').click()
# assert driver.find_element('id', 'ui-datepicker-div').is_displayed()
# month = driver.find_element('class name', 'ui-datepicker-month').text
# year = driver.find_element('class name', 'ui-datepicker-year').text
# while not (month.__eq__('February') and year.__eq__('2024')):
#     driver.find_element('xpath', '//a[@data-handler="next"]').click()
#     month = driver.find_element('class name', 'ui-datepicker-month').text
#     year = driver.find_element('class name', 'ui-datepicker-year').text
# date = driver.find_element('link text', '6')
# date.click()

# verify actual date is matching the expected one:
# driver.get('https://seleniumpractise.blogspot.com/2016/08/how-to-handle-calendar-in-selenium.html')
# driver.find_element('id', 'datepicker').click()
# assert driver.find_element('id', 'ui-datepicker-div').is_displayed()
# expected_date = '6-February-2024'
# month = driver.find_element('class name', 'ui-datepicker-month').text
# year = driver.find_element('class name', 'ui-datepicker-year').text
# while not (month.__eq__('February') and year.__eq__('2024')):
#     driver.find_element('xpath', '//a[@data-handler="next"]').click()
#     month = driver.find_element('class name', 'ui-datepicker-month').text
#     year = driver.find_element('class name', 'ui-datepicker-year').text
# date = driver.find_element('link text', '6')
# date.click()
# actual_date = date.text + '-' + month + '-' + year
# assert actual_date == expected_date
# print('The actual date is been selected as expected date.', f'The selected date is {actual_date}', sep='\n')

# Select the date using function:
# def select_date(expected_date: str, expected_month: str, expected_year: str):
#     month = driver.find_element('class name', 'ui-datepicker-month').text
#     year = driver.find_element('class name', 'ui-datepicker-year').text
#     while not (month.__eq__(expected_month) and year.__eq__(expected_year)):
#         driver.find_element('xpath', '//a[@data-handler="next"]').click()
#         month = driver.find_element('class name', 'ui-datepicker-month').text
#         year = driver.find_element('class name', 'ui-datepicker-year').text
#     date = driver.find_element('link text', expected_date)
#     date.click()
#     actual_date = date.text + '-' + month + '-' + year
#     return actual_date

# driver.get('https://seleniumpractise.blogspot.com/2016/08/how-to-handle-calendar-in-selenium.html')
# driver.find_element('id', 'datepicker').click()
# assert driver.find_element('id', 'ui-datepicker-div').is_displayed()
# print(select_date('23', 'December', '2023'))

# Past date:
# driver.get('https://seleniumpractise.blogspot.com/2016/08/how-to-handle-calendar-in-selenium.html')
# driver.find_element('id', 'datepicker').click()
# assert driver.find_element('id', 'ui-datepicker-div').is_displayed()
# month = driver.find_element('class name', 'ui-datepicker-month').text
# year = driver.find_element('class name', 'ui-datepicker-year').text
# while not (month.__eq__('February') and year.__eq__('2002')):
#     driver.find_element('xpath', '//a[@data-handler="prev"]').click()
#     month = driver.find_element('class name', 'ui-datepicker-month').text
#     year = driver.find_element('class name', 'ui-datepicker-year').text
# date = driver.find_element('link text', '6')
# date.click()

# Select the both the past and future dates:
# driver.get('https://seleniumpractise.blogspot.com/2016/08/how-to-handle-calendar-in-selenium.html')
# driver.find_element('id', 'datepicker').click()
# assert driver.find_element('id', 'ui-datepicker-div').is_displayed()
# expected_date = '06-02-2022'
# formatted_date = datetime.strptime(expected_date, '%d-%m-%Y')
# expected_day, expected_month, expected_year = formatted_date.day, formatted_date.month, formatted_date.year
# month_list = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6, 'July': 7, 'August': 8,
#               'September': 9, 'October': 10, 'November': 11, 'December': 12}
# current_month = driver.find_element('class name', 'ui-datepicker-month').text
# cur_month = month_list[current_month]
# cur_year = int(driver.find_element('class name', 'ui-datepicker-year').text)
#
# while cur_year < expected_year or cur_month < expected_month:
#     driver.find_element('xpath', '//a[@data-handler="next"]').click()
#     current_month = driver.find_element('class name', 'ui-datepicker-month').text
#     cur_month = month_list[current_month]
#     cur_year = int(driver.find_element('class name', 'ui-datepicker-year').text)
#
# while cur_year > expected_year or cur_month > expected_month:
#     driver.find_element('xpath', '//a[@data-handler="prev"]').click()
#     current_month = driver.find_element('class name', 'ui-datepicker-month').text
#     cur_month = month_list[current_month]
#     cur_year = int(driver.find_element('class name', 'ui-datepicker-year').text)
# driver.find_element('link text', f'{str(expected_day)}').click()

# Select date using Javascript command:
# driver.get('https://seleniumpractise.blogspot.com/2016/08/how-to-handle-calendar-in-selenium.html')
# driver.execute_script(f'document.getElementById("datepicker").value="06/02/2002"')

# Note: It's not recommended to use this javascript command only if there's no way to handle this calendar, we should
# go for this way to handle the calendar.

# Calendar type 2:
# In this calendar, We can select the date from present and future.
# Here, we've a direct option to change the year.
# In this calendar type, The dates of past, present and future month are displayed.

# driver.get('https://www.path2usa.com/travel-companion/')
# actions.scroll_by_amount(0, 1000).pause(3).perform()
# driver.find_element('id', 'form-field-travel_comp_date').click()
# month = driver.find_element('class name', 'cur-month').text.strip()
# expected_month = 'February'
# while not (month.__eq__(expected_month)):
#     driver.find_element('class name', 'flatpickr-next-month').click()
#     actions.pause(2).perform()
#     month = driver.find_element('class name', 'cur-month').text.strip()
# driver.find_element('xpath', f'//span[text() = "6" and contains(@aria-label,"{expected_month}")]').click()

# driver.get('https://www.goibibo.com/')
# driver.find_element('xpath', '//span[@role="presentation"]').click()
# driver.find_element('xpath', '//span[text()="Departure"]').click()
# current_month = driver.find_element('xpath', '//div[@class="DayPicker-Caption"]').text
# while not current_month.__eq__('July 2024'):
#     driver.find_element('xpath', '//span[@aria-label="Next Month"]').click()
#     current_month = driver.find_element('xpath', '//div[@class="DayPicker-Caption"]').text
# driver.find_element('xpath', '//p[text()="12"]').click()
# driver.find_element('xpath', '//span[text()="Done"]').click()

# Calendar type 3:
# In this calendar, We can select the date from present and future along with this we can even select the time
# in hours and minutes also.
# Here, We can automate some calendar and soe cannot in such cases we've to enter the data directly.
# In this calendar type, The dates of past, present and future and time are displayed.

# driver.get('https://demo.guru99.com/test/')
# date_time_box = driver.find_element('name', 'bdaytime')
# date_time_box.send_keys('06022002', Keys.TAB, '0830AM')
# sleep(3)
# date_time_box.submit()
# assert driver.find_element('xpath', '//div[contains(text(), "Birth Date")]').is_displayed()

# driver.get('https://www.hyrtutorials.com/p/calendar-practice.html')
# driver.execute_script('const elements = document.getElementsByClassName("adsbygoogle adsbygoogle-noablate");'
#                       'while (elements.length > 0) elements[0].remove()')
# driver.find_element('class name', 'ui-datepicker-trigger').click()
# expected_date = '06-02-2022'
# formatted_date = datetime.strptime(expected_date, '%d-%m-%Y')
# expected_day, expected_month, expected_year = formatted_date.day, formatted_date.month, formatted_date.year
# month_list = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6, 'July': 7, 'August': 8,
#               'September': 9, 'October': 10, 'November': 11, 'December': 12}
# cur_month = driver.find_element('class name', 'ui-datepicker-month').text
# current_month = month_list[cur_month]
# current_year = int(driver.find_element('class name', 'ui-datepicker-year').text)
#
# while current_year < expected_year or current_month < expected_month:
#     driver.find_element('xpath', '//span[text() = "Next"]').click()
#     cur_month = driver.find_element('class name', 'ui-datepicker-month').text
#     current_month = month_list[cur_month]
#     current_year = int(driver.find_element('class name', 'ui-datepicker-year').text)
#
# while current_year > expected_year or current_month > expected_month:
#     driver.find_element('xpath', '//span[text() = "Prev"]').click()
#     cur_month = driver.find_element('class name', 'ui-datepicker-month').text
#     current_month = month_list[cur_month]
#     current_year = int(driver.find_element('class name', 'ui-datepicker-year').text)
# driver.find_element('link text', f'{str(expected_day)}').click()

# or
# driver.find_element('id', 'sixth_date_picker').send_keys('02/06/2002')

# Calendar type 4:
# This is quite similar to calendar 1, this calendar is combined with dates block and month and year dropdowns.
# This calendars are preloaded one.

# driver.get('https://www.hyrtutorials.com/p/calendar-practice.html')
# driver.find_element('id', 'third_date_picker').click()
# Select(driver.find_element('xpath', '//select[@data-handler="selectMonth"]')).select_by_visible_text('Feb')
# Select(driver.find_element('xpath', '//select[@data-handler="selectYear"]')).select_by_visible_text('2024')
# driver.find_element('xpath', '//a[text() = "6"]').click()

# Calendar type 5:
# This type of calendar, has certain dates and months within that only we've to select the date.
# Other dates are frozen for certain period of time.
# This kind of calendars are used in movie ticket booking application.

# driver.get('https://www.hyrtutorials.com/p/calendar-practice.html')
# driver.find_element('id', 'fifth_date_picker').click()
# current_month = driver.find_element('class name', 'ui-datepicker-month').text
# current_year = driver.find_element('class name', 'ui-datepicker-year').text
#
# while not (current_year.__eq__('2024') and current_month.__eq__('January')):
#     driver.find_element('xpath', '//span[text() = "Next"]').click()
#     current_month = driver.find_element('class name', 'ui-datepicker-month').text
#     current_year = driver.find_element('class name', 'ui-datepicker-year').text
# driver.find_element('link text', '6').click()

driver.quit()
"""
