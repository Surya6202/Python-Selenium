'''
standard list box : If the tagname of the listbox is select tag.

Can locate the elements using three methods
1. select by index : Index number starts from 1
2. select by value : The value attribute present in the html code
3. select by visible text


'''
#-----------------------------------------------------
import time

# from selenium import webdriver
# from selenium.webdriver.support.ui import Select
#
# ## Select is a class
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=opts)
#
# driver.get(r'C:\Users\Ramya\PycharmProjects\selenium_QCO_SOFPSD_E3\files\demo.html')
# time.sleep(3)
#
# list_box = driver.find_element('xpath', '//select[@id="standard_cars"]')
# select_object = Select(list_box)

## by index
# select_object.select_by_index(2)
# time.sleep(2)
# select_object.select_by_index(9)
# time.sleep(2)
# select_object.select_by_index(3)

# ## by value
# select_object.select_by_value('toy')
# time.sleep(2)
# select_object.select_by_value('hda')
# time.sleep(2)
# select_object.select_by_value('lr')

## visible text
# select_object.select_by_visible_text('Jaguar')
# time.sleep(2)
# select_object.select_by_visible_text('Ford')
# time.sleep(2)
# select_object.select_by_visible_text('Volvo')

#------------------------------------------------------------------------
# from selenium import webdriver
# from selenium.webdriver.support.ui import Select
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=opts)
#
# driver.get(r'C:\Users\Ramya\PycharmProjects\selenium_QCO_SOFPSD_E3\files\demo.html')
# time.sleep(3)
#
# list_box = driver.find_element('xpath', '//select[@id="standard_cars"]')
# select_obj = Select(list_box)
#
# ## To get all the elements in the listbox
#
# ## options is a property. It will give all the elements present inside the listbox
#
# all_cars = select_obj.options
# print(all_cars)
#
# for car in all_cars:
#     print(car.text)

#-----------------------------------------------------------------------
'''select all the cars in demo.html'''
#
# from selenium import webdriver
# from selenium.webdriver.support.ui import Select
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=opts)
#
# driver.get(r'C:\Users\Ramya\PycharmProjects\selenium_QCO_SOFPSD_E3\files\demo.html')
# time.sleep(3)
#
# list_box = driver.find_element('xpath', '//select[@id="standard_cars"]')
# print(list_box)
# select_obj = Select(list_box)
#
# all_cars = select_obj.options       ## list of webelements
# print(all_cars)
#
# for car in all_cars:
#     print(car.text)

#-------------------------------------------------------------------------
## selecting the elements without using select class
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=opts)
#
# driver.get(r'C:\Users\Ramya\PycharmProjects\selenium_QCO_SOFPSD_E3\files\demo.html')
# time.sleep(3)
#
# driver.find_element('xpath', '//select[@id="standard_cars"]').click()
# time.sleep(2)
# driver.find_element('xpath', '(//option[text()="Ford"])[1]').click()

#---------------------------------------------------------------------------
## Selecting the date, month and year in facebook signup page
#
from selenium import webdriver
from selenium.webdriver.support.ui import Select

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=opts)

driver.get('https://www.facebook.com/signup')
time.sleep(3)

date_ = driver.find_element('xpath', '//select[@name="birthday_day"]')
select_obj_date = Select(date_)

month_ = driver.find_element('xpath', '//select[@name="birthday_month"]')
select_obj_month = Select(month_)

year_ = driver.find_element('xpath', '//select[@name="birthday_year"]')
select_obj_year = Select(year_)

## select by index
select_obj_date.select_by_index(14)
time.sleep(2)
select_obj_month.select_by_index(5)
time.sleep(2)
select_obj_year.select_by_index(25)


## select by value
select_obj_date.select_by_value('8')
time.sleep(2)
select_obj_month.select_by_value('8')
time.sleep(2)
select_obj_year.select_by_value('1988')


## select by visible text
select_obj_date.select_by_visible_text('4')
time.sleep(2)
select_obj_month.select_by_visible_text('Jan')
time.sleep(2)
select_obj_year.select_by_visible_text('1963')

###---------------
### To get the list of all the elements present inside the listbox

# all_months = select_obj_month.options
# print(all_months)       ## list of webelements
#
# for month in all_months:
#     print(month.text)

#-------------------------------------------------------------------
## IRCTC

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=opts)
#
# driver.get('https://www.irctc.co.in/nget/train-search')
# time.sleep(3)
#
# driver.find_element('xpath', '(//div[@role="button"])[1]').click()
# time.sleep(3)
# driver.find_element('xpath', '//span[text()="Vistadome AC (EV)"]').click()
# time.sleep(3)
# driver.find_element('xpath', '(//div[@role="button"])[2]').click()
# time.sleep(2)
# driver.find_element('xpath', '//span[text()="TATKAL"]').click()

#---------------------------------------------------------------------------
## ASSIGNMENT
## 1. Select the country in  https://testautomationpractice.blogspot.com/
## 2. Fill the details  in https://www.shaadi.com/.
## 3. Go to https://www.naukri.com/, fill in the details and search for job
## 4. Go to https://www.airbnb.co.in/, get all the places and price
## 5. In https://www.shaadi.com/, get the list of all the religions and mother tongue 
#---------------------------------------------------------------------------

## multiselect listbox

from selenium import webdriver
from selenium.webdriver.support.ui import Select

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=opts)

driver.get('https://testautomationpractice.blogspot.com/')
time.sleep(3)

colors = driver.find_element('xpath', '//select[@id="colors"]')
select_obj_colors =  Select(colors)

## By index
select_obj_colors.select_by_index(1)
time.sleep(2)
select_obj_colors.select_by_index(2)
time.sleep(2)
select_obj_colors.select_by_index(4)



