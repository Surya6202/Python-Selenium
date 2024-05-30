'''
selenium --> to automate web applications
open source, platform independent

8 locators
id, name, class name, tag name, link text, partial link text, css selector, xpath

webelement method
driver.find_element('locator_name', 'locator_value')

css selector = tagname[attr_name="attr_value"]

xpath : Will give unique match for any webelement
i) attr_name and attr_value
        //tagname[@attr_name="attr_value"]

ii) text
        //tagname[text()="text"]

iii) group indexing
        (//tagname[@attr_name="attr_value"])[index_num]
        (//tagname[text()="text"])[index_number]

iv) contains
        //tagname[contains(text(), "text")]

v) dependent/independent
        * identify dependent/independent element
        * write the xpath of the independent element
        * traverse back till we find common match for both dependent and independent element(/..)
        * write the xpath of the dependent element

find_elements()
        driver.find_elements('locator_name', 'locator_value')

#---------------------------------------------------------------------------
listboxes : if the tagname is select, standard listbox --> Select class
--> from selenium.webdriver.support.ui import Select

* locate entire listbox which is having select tag

select_object = Select(listbox)
* by value
* by index
* by visible text

select_object.option --> option is a property. Will give the list of all the elements present in the listbox

#-----------------------------------------------------------------------------
alerts : not inspectable. We have to switch the control from webpage to the alert

alert_obj = chrome_driver.switch_to.alert
alert_obj.accept()
alert_obj.dismiss()

1. simple
2. confirmation
3. authentication : https://username:password@testautomationpractice.blogspot.com/
4. file upload

#------------------------------------------------------------------------------
Action chains : To perform low level operations
--> from selenium.webdriver.common.action_chains import ActionChains
--> from selenium.webdriver.common.keys import Keys

action_chains --> module
ActionChains --> class

action_chain_object = ActionChains(driver)

## mouse hovering
element = chrome_driver.find_element('', '')
act_obj.move_to_element(element).perform()

## double click
act_obj.double_click(element)

## right click
act_obj.context_click(element)

## scroll
act_obj.scroll_to_element(element)

## drag and drop
draggable_ele = chrome_driver.find_element('', '')
droppable_ele = chrome_driver.find_element('', '')
act_obj.drag_and_drop(draggable_ele, droppable_ele).perform()

##
act_obj.key_down(Keys.CONTROL).perform()
act_obj.send_keys('A')
act_obj.key_up(Keys.CONTROL).perform()

#---------------------------------------------------------------------------
iframe
chrome_driver.switch_to.frame(id/name/xpath)

#--------------------------------------------------------------------------
synchronization : matching rhe speed of the webdriver to that of webapplication
unconditional : No conditions. time.sleep(seconds)
conditional
    i) implicit_wait : internally conditions are taken.
                        driver.implicitly_wait(seconds)
    ii) explicit_wait : pass the conditions explicitly
            --> from selenium.webdriver.support.ui import WebDriverWait
            --> from selenium.webdriver.support import expected_conditions
                wait_obj = WebDriverWait(chrome_driver, 30)

#-------------------------------------------------------------------------

'''
import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

chrome_driver = webdriver.Chrome(options=opts)

chrome_driver.get('https://www.makemytrip.com/')
time.sleep(2)
chrome_driver.save_screenshot(r"C:\Users\Ramya\OneDrive\Desktop\selenium_practise__\screenshot.png")
# firefox_driver = webdriver.Firefox()

# opts = webdriver.EdgeOptions()
# opts.add_experimental_option("detach", True)
#
# edge_driver = webdriver.Edge(options=opts)

# chrome_driver.get('url')
#
# chrome_driver.find_element('id', 'input').send_keys('')
#
#
# alert_obj = chrome_driver.switch_to.alert
act_obj = ActionChains(chrome_driver)
#
# ## mouse hovering
# element = chrome_driver.find_element('', '')
# act_obj.move_to_element(element).perform()
#
# ## double click
# act_obj.double_click(element)
#
# ## right click
# act_obj.context_click(element)
#
# ## scroll
# act_obj.scroll_to_element(element)
#
# ## drag and drop
# draggable_ele = chrome_driver.find_element('', '')
# droppable_ele = chrome_driver.find_element('', '')
# act_obj.drag_and_drop(draggable_ele, droppable_ele).perform()
#
# ##
# act_obj.key_down(Keys.CONTROL).perform()
# act_obj.send_keys('A')
# act_obj.key_up(Keys.CONTROL).perform()
#
# chrome_driver.switch_to.frame()

#----------------------------------------------------------------------------------

# chrome_driver.get('https://www.myntra.com/')
# time.sleep(2)
#
# element = chrome_driver.find_element('xpath', '(//a[text()="Home & Living"])[1]')
# act_obj.move_to_element(element).perform()
# time.sleep(2)
#
# chrome_driver.find_element('xpath', '//a[text()="Aromas & Candles"]').click()
# time.sleep(2)
#
# chrome_driver.find_element('xpath', '//h4[@class="product-product"]').click()
#
# handles = chrome_driver.window_handles
# print(handles)          ## [parent, child]
#
# chrome_driver.switch_to.window(handles[1])
# time.sleep(1)
#
# chrome_driver.find_element('xpath', '//div[text()="ADD TO BAG"]').click()
# time.sleep(2)
#
# chrome_driver.switch_to.window(handles[0])
# time.sleep(1)
#
# chrome_driver.find_element('xpath', '(//h4[@class="product-product"])[2]').click()
#
# handles1 = chrome_driver.window_handles
# print(handles1)
#
# chrome_driver.switch_to.window(handles1[2])
# time.sleep(2)
#
# chrome_driver.find_element('xpath', '//div[text()="ADD TO BAG"]').click()
# time.sleep(3)
#
# # chrome_driver.close()       ## closes the active window
# chrome_driver.quit()

#--------------------------------------------------------------------

# chrome_driver.get('https://www.makemytrip.com/')
# time.sleep(3)
#
# chrome_driver.find_element('xpath', '//span[text()="Departure"]').click()
# time.sleep(6)
#
# month = chrome_driver.find_element('xpath', '//div[@class="DayPicker-Caption"]')
# for ele in range(1, 12):
#     if month.text == 'April 2024':
#         chrome_driver.find_element('xpath', '//p[text()="10"]').click()
#         break
#     else:
#         chrome_driver.find_element('xpath', '//span[@aria-label="Next Month"]').click()
#     time.sleep(1)

#-----------------------------------------------------------------



















