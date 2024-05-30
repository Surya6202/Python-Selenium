## To  perform any low level operations we use ActionChains
import time

## mouse_hovering -->  move_to_element() is the attribute used for mouse hovering operations

# ## EG1
# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# 4
# driver = webdriver.Chrome(options=opts)
#
# action_chain_obj = ActionChains(driver)
#
# driver.get('https://www.myntra.com/')
# time.sleep(3)
#
# element = driver.find_element('xpath', '(//a[text()="Home & Living"])[1]')
#
# action_chain_obj.move_to_element(element).perform()
# ## To perform the hovering actions, we should give .perform()
#
# ##
# # EG2
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=opts)
#
# act_obj = ActionChains(driver)
#
# driver.get('https://www.flipkart.com/')
# time.sleep(3)
#
# fashion_element = driver.find_element('xpath', '//span[text()="Fashion"]')
# act_obj.move_to_element(fashion_element).perform()
# time.sleep(3)
#
# home_furniture_element = driver.find_element('xpath', '//span[text()="Home & Furniture"]')
# act_obj.move_to_element(home_furniture_element).perform()


#------------------------------------------------------------------------
## ASSIGNMENT
## 1. Go to https://www.foundit.in/, hover on skillsets and click on Python
## 2. In ajio, hover to the home and kitchen and click on wall decor

#--------------------------------------------------------------------------
# ## To double click
#
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=opts)
# act_obj = ActionChains(driver)
#
# driver.get('https://testautomationpractice.blogspot.com/')
# time.sleep(3)
#
# element = driver.find_element('xpath', '//button[text()="Copy Text"]')
# act_obj.double_click(element).perform()
# time.sleep(2)
#
# ele = driver.find_element('xpath', '//label[text()="Name:"]')
# act_obj.double_click(ele).perform()

#---------------------------------------------------------------------
## To right click on any element : context_click()

# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=opts)
# act_obj = ActionChains(driver)
#
# driver.get('https://www.foundit.in/')
# time.sleep(3)
#
# element = driver.find_element('xpath', '//div[contains(text(), "Register Now")]')
# act_obj.context_click(element).perform()

#----------------------------------------------------------------------
## drag and drop
# ##EG1
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=opts)
# act_obj = ActionChains(driver)
#
# driver.get('https://testautomationpractice.blogspot.com/')
# time.sleep(3)
#
# drag = driver.find_element('xpath', '//p[text()="Drag me to my target"]')
# drop = driver.find_element('xpath', '//div[@id="droppable"]')
#
# act_obj.drag_and_drop(drag, drop).perform()
#
# #-------------------------------------------------------------------
# ## ASSIGNMENT
# ## 1. http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html . Perform drag and drop operations
#
#-----------------------------------------------------------------------
### ASSIGNMENT
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=opts)
# act_obj = ActionChains(driver)
#
# driver.get('http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html')
# time.sleep(3)
#
# for i in range(1, 8):
#     source = driver.find_element('xpath', f'//div[@id="box{i}"]')
#     target = driver.find_element('xpath', f'//div[@id="box10{i}"]')
#
#     act_obj.drag_and_drop(source, target).perform()

##
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=opts)
# act_obj = ActionChains(driver)
#
# driver.get('http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html')
# time.sleep(3)
#
# capitals_list = []
# capitals = driver.find_elements('xpath', '//div[@class="dragableBox"]')
# for city in capitals:
#     if len(city.text) != 0:
#         capitals_list.append(city.text)
#
# countries_list = []
# countries = driver.find_elements('xpath', '//div[@class="dragableBoxRight"]')
# for country in countries:
#     countries_list.append(country.text)
#
#
# print(capitals_list)
# print(countries_list)

# #----------------------------------------------------------------------
# ## To scroll up and down
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=opts)
# act_obj = ActionChains(driver)
#
# driver.get('https://testautomationpractice.blogspot.com/')
# time.sleep(2)
#
# act_obj.send_keys(Keys.PAGE_DOWN).perform()
# time.sleep(2)
# act_obj.send_keys(Keys.PAGE_UP).perform()
# time.sleep(2)
# act_obj.send_keys(Keys.ARROW_DOWN).perform()
#
# # To scroll to a particular element
# element = driver.find_element('xpath', '//h2[text()="Web Table"]')
# act_obj.move_to_element(element).perform()

#_--------------------------------------------------------------
## To select everything present in the webpage

# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=opts)
# act_obj = ActionChains(driver)
#
# driver.get('https://testautomationpractice.blogspot.com/')
# time.sleep(2)
#
# act_obj.key_down(Keys.CONTROL).perform()
# act_obj.send_keys('A').perform()
# act_obj.key_up(Keys.CONTROL).perform()

#-------------------------------------------------------------------------

















































































