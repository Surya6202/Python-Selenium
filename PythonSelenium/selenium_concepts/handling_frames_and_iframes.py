"""
from selenium import webdriver
from utilities import chrome_options

driver = webdriver.Chrome(chrome_options)
driver.implicitly_wait(20)

# Frames:
# It's used to divide your browser window into multiple sections where each section can load a separate HTML document.
# There is a tag called frameset tag which is used to define how to divide the window into frames.

# Iframes:
# An iframe is also known as an inline frame.
# It is a tag used in HTML to embed an HTML document within a parent HTML document.
# An iframe tag is defined using <iframe></iframe> tags.
# A webpage may have many frames or may not.

# Difference between frame and iframe:
# The frame enables a developer to split the screen horizontally or vertically by using the frameset tag and it divides
# the webpage into multiple sections that each section can load a separate HTML document.
# The iframes are mainly used to insert content from external sources and They can float within the webpage, which means
# one can position an iframe at a specific position on a web page.

# Note:
# Frame and frameset tags are deprecated as they are no longer supported by HTML.

# To identify a frame in the webpage we've different ways to do it:
# 1) press 'ctrl+shift+i' or right click on the webpage and click on inspect, we'll get source code and press 'ctrl+f'
# and enter '//iframe' that will show how many iframes are there in the webpage.
# 2) Right click on the webpage and check the options, if find the options 'view Frame source or Reload Frame',
# the page includes frames.
# 3) Right click on the webpage and click on 'view page source' and press ctrl+f and enter iframe, check for '<iframe'.
# 4) By looking at the user interface, We can check whether the frame is there or not.

# By default the driver control will be in the default content to perform the actions on that frame we've to follow the
# steps:
# 1) Identify the target frame inside the webpage.
# 2) Transfer/ Switch the driver control to the target frame.
# 3) Then perform the required action.

# Note:
# 1) If we try to perform any action on the target webelement without swtiching the driver control, we'll get
# 'NoSuchElementException'.

# driver.get('https://www.globalsqa.com/demo-site/frames-and-windows/#iFrame')
# try:
#     driver.find_element('xpath', '//img[@alt="Selenium Online Training"]').click()
# except NoSuchElementException:
#     print('NoSuchElementException is handled')
# finally:
#     print('This target element is present in the frame')

# 2) If we try to transfer driver control to the target frame which doesn't exist in the webpage, we'll get
# 'NoSuchFrameException'.

# driver.get('https://www.facebook.com/')
# try:
#     driver.switch_to.frame(0)
#
# except NoSuchFrameException:
#     print('NoSuchFrameException is handled')
# finally:
#     print('This webpage doesn\'t have the frame')

# To handle the frames, We've to switch the driver control to the target frame.
# We can the switch the driver control by using a method called frame().
# Upon switch_to property we should call this method.
# This method accepts only one argument which can be an index or locators like id or name or frame webelement.
# This frame method is an example for method overloading(same name with differ in arguments).

# 1) frame by index:
# Here, We're switching the driver control based on the index position of the frame present in the webpage and perform
# the required operation.
# We've to pass the index position as an argument.
# Unlike xpath here the index position will start from 0.

# driver.get('https://the-internet.herokuapp.com/iframe')
# driver.switch_to.frame(0)
# para = driver.find_element('xpath', '//body/p')
# para.clear()
# para.send_keys('Rajanandini')

# 2) frame by id locator:
# Here, We're switching the driver control to the frame by passing the id attribute value as an argument.

# driver.get('https://blogpendingtasks.blogspot.com/p/switchtoframeusingwebelement.html')
# driver.switch_to.frame('comment-editor')
# driver.find_element('xpath', '//span[contains(text(), "Sign in")] ').click()

# 3) frame by name locator:
# Here, We're switching the driver control to the frame by passing the name attribute value as an argument.

# driver.get('https://docs.oracle.com/javase/8/docs/api/')
# driver.switch_to.frame('classFrame')
# driver.find_element('link text', 'Description').click()

# 4) frame by webelement:
# Here, We're switching the driver control to the frame by passing the frame webelement as an argument.

# driver.get('https://www.globalsqa.com/demo-site/frames-and-windows/#iFrame')
# driver.execute_script('const elements = document.getElementsByClassName("adsbygoogle adsbygoogle-noablate"); '
#                       'while (elements.length > 0) elements[0].remove()')
# frame_ele = driver.find_element('name', 'globalSqa')
# frame_ele.location_once_scrolled_into_view
# driver.switch_to.frame(frame_ele)
# ele = driver.find_element('xpath', '//img[@alt = "Manual Online Testing Training"]')
# ele.click()

# If the webpage has multiple iframes and we should switch to other iframes, We can't directly switch to other frames.
# We've to switch the driver control to either another frame or default frame and then we can switch the driver control
# to other frames.
# To perform this operation we have two methods:
# 1) parent_frame()
# 2) default_content()

# parent_frame method will transfer the driver control to the immediate previous frame or default frame (main document).

# driver.get('https://letcode.in/frame')
# driver.switch_to.frame('firstFr')
# driver.find_element('name', 'fname').send_keys('Surya')
# driver.find_element('name', 'lname').send_keys('Rajendran')
# child_frame = driver.find_element('xpath', '//iframe[@src="innerFrame"]')
# driver.switch_to.frame(child_frame)
# driver.find_element('name', 'email').send_keys('suryar6202@gmail.com')
# driver.switch_to.parent_frame()
# driver.find_element('name', 'lname').clear()
# driver.find_element('name', 'lname').send_keys('R')
# para_text = driver.find_element('xpath', '//p[@class = "title has-text-info"]').text
# assert 'Surya R' in para_text

# default_content method will transfer the driver control to either default frame (main document) which contains
# iframes.

# driver.get('https://docs.oracle.com/javase/8/docs/api/')
# driver.switch_to.frame('classFrame')
# print(driver.find_element('link text', 'Description').text)
# driver.switch_to.default_content()
# driver.switch_to.frame('packageListFrame')
# driver.find_element('link text', 'java.sql').click()

# Nested frames:
# A single frame or a group of frames present inside another frame is called nested frames.

# driver.get('https://the-internet.herokuapp.com/nested_frames')
#
# # Transfering the driver control from default frame to child
# driver.switch_to.frame('frame-top')
#
# # Transfering the driver control from parent to child
# driver.switch_to.frame('frame-left')
# print(driver.find_element('xpath', '//body[contains(text(), "LEFT")]').text)
#
# # Transfering the driver control from child to parent
# driver.switch_to.parent_frame()
#
# # Transfering the driver control from parent to child
# driver.switch_to.frame('frame-middle')
# print(driver.find_element('id', 'content').text)
#
# # Transfering the driver control from child to parent
# driver.switch_to.parent_frame()
#
# # Transfering the driver control from parent to child
# driver.switch_to.frame('frame-right')
# print(driver.find_element('xpath', '//body[contains(text(), "RIGHT")]').text)
#
# # Transfering the driver control from child to default frame (main document)
# driver.switch_to.default_content()
#
# # Transfering the driver control from default frame to child
# driver.switch_to.frame('frame-bottom')
# print(driver.find_element('xpath', '//body[contains(text(), "BOTTOM")]').text)

driver.quit()
"""
