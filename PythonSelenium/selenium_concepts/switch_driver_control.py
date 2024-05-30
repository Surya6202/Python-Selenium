"""
from time import sleep

from selenium.webdriver import Keys, ActionChains
from selenium import webdriver

from utilities import chrome_options

driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(20)
actions = ActionChains(driver)

# switch_to:
# It's a property in the webdriver module that is used to switch or transfer the driver control to the window, tab,
# frame, alert popups and active element.
# Th return type of this property is SwitchTo which is an object containing all options to switch the driver control
# or focus of the window.
# upon driver reference, we sould call this property and upon this we can access the options of SwitchTo object
# and they're alert, active_element, window, new_window, frame, parent_frame and default_content.
# By using this property, we can handle alert popups, windows, active element and frames.

switch = driver.switch_to

# 1. alert:
# It's a property of SwitchTo class which switches the driver control to the alert popup.
# The return type of this property is Alert.
# The Alert class provides several methods, function and property to handle the alert popup.
# TThey're accept(), dismiss(), send_keys(), text etc...

# driver.get('https://omayo.blogspot.com/')
# search_button = driver.find_element('id', 'alert1')
# search_button.click()
# switch.alert.dismiss()

# 2. window():
# It's a method of SwitchTo class which switches the driver control to the window or tab.
# We've to pass the window handle as an argument in the form of string.
# The return type of this method is None.

# driver.get('https://omayo.blogspot.com/')
# actions.key_down(Keys.SHIFT).click(driver.find_element('id', 'link1')).key_up(Keys.SHIFT).perform()
# window_ids = driver.window_handles
# switch.window(window_ids[0])
# print(driver.title, driver.current_url, '', sep='\n')
# driver.close()
# switch.window(window_ids[1])
# print(driver.title, driver.current_url, sep='\n')

# 3. new_window():
# It's a method of SwitchTo class which will create a new window or tab and transfers the driver control to that
# new window or tab.
# This method accepts type hint as an argument in the form of string and the type hint would be a 'window' or 'tab'.
# The return type of this method is None.

# driver.get('https://www.netflix.com')
# switch.new_window('tab')
# driver.get('https://www.hotstar.com/')
# switch.new_window('window')
# driver.get('https://www.zee5.com')
# window_ids = driver.window_handles
# for window_id in window_ids:
#     switch.window(window_id)
#     print(driver.current_url, driver.title, sep='\n')
# driver.quit()

# 4. frame():
# It's a method of SwitchTo class which switches the driver to the iframe based on the argument.
# The argument for this method is index position or id locator or name locator or frame webelement.
# The return type of this method is None.

# 5. parent_frame():
# It's a method of SwitchTo class which switches the driver to the immediate parent frame or default frame.
# The return type of this method is None.

# 6. default_content():
# It's a method of SwitchTo class which switches the driver to the default frame.
# The return type of this method is None.

# driver.get('https://the-internet.herokuapp.com/nested_frames')
# # Transfering the driver control from default frame to child
# switch.frame('frame-top')
# # Transfering the driver control from parent to child
# switch.frame('frame-left')
# print(driver.find_element('xpath', '//body[contains(text(), "LEFT")]').text)
# # Transfering the driver control from child to parent
# switch.parent_frame()
# # Transfering the driver control from parent to child
# switch.frame('frame-middle')
# print(driver.find_element('id', 'content').text)
# # Transfering the driver control from child to parent
# switch.parent_frame()
# # Transfering the driver control from parent to child
# switch.frame('frame-right')
# print(driver.find_element('xpath', '//body[contains(text(), "RIGHT")]').text)
# # Transfering the driver control from child to default frame (main document)
# switch.default_content()
# # Transfering the driver control from default frame to child
# switch.frame('frame-bottom')
# print(driver.find_element('xpath', '//body[contains(text(), "BOTTOM")]').text)

# 7. active_element:
# It's a property of SwitchTo class that switches the driver control to the active element.
# Active Element: It's the element which is enabled by default in the webpage.
# With help of Keys class, ActionChains class and webelement methods we can handle it.
# The return type of this property is webelement so we can perform the required webelement opertaions on it.

# driver.get('https://www.facebook.com/')
# switch.active_element.send_keys('Surya123@gmail.com', Keys.TAB, 'Surya@123', Keys.TAB, Keys.TAB, Keys.ENTER)

driver.quit()
"""
