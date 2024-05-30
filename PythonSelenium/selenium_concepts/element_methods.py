"""
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.support.color import Color
from utilities import chrome_options

driver = webdriver.Chrome(options=chrome_options)

driver.get('https://omayo.blogspot.com/2013/05/page-one.html')
driver.implicitly_wait(30)

# Webelements are the elements that are present in the webpage.
# It's also called as UI elements.
# It can be a textfield, button, link, drop-down etc...
# Based on the operations to be performed on webelements, Webelement has certain methods and properties:
# clear(), click(), find_element(), find_elements(), get_attribute(), is_displayed(), is_enabled(), is_selected(),
# location, location_once_scrolled_into_view, rect, screenshot(), send_keys(), size, submit(), tag_name, text,
# value_of_css_property()

# 1) clear():
# It'll remove/ clear the default/ pre-entered text in the textbox or clear the entered text.
# It'll clear all the text in that textbox.
# The return type of this method is None.

# driver.find_element('id', 'textbox1').clear()

# 2) click():
# It's used to click on the target webelement like button, textfield, checkbox, link etc...
# It's has the capacity to scroll the webpage.
# It won't wait until the next page gets loaded.
# If the element is hidden by another element, then we'll get 'ElementClickInterceptedException'.
# We can handle this exception by handling obscured element (An element which hides another element).
# The return type of this method is None.

# driver.find_element('partial link text', 'Selenium143').click()

# 3) find_element():
# find_element() which finds an element in webpage which accepts By strategy and locator as an argument.
# It'll start searching the element in the html document from beginning to end until the target element is found.
# Syntax: driver.find_element('locator_name', 'locator_value')
# If the element is found, it'll return the webelement where we can perform further actions on it.
# If the element is not found, it'll end up with an exception called 'NoSuchElementException'.
# If the given locator identifies multiple elements, it'll return the first matching element.
# The return type of this method is webelement.

# 4) find_elements():
# find_elements() which finds multiple elements in webpage, which accepts By strategy and locator as an argument.
# Stores all the matching webelements inside the list collection.
# Syntax: driver.find_elements('locator_name', 'locator_value')
# If the given locator strategy is not locating any webelement, then it returns an empty list.
# It can be used to verify the total number of websites present in the webpage.
# It can be used to handle the auto-suggestions.
# The return type of this method is list[webelement].

# 5) get_attribute():
# We've to pass the attribute name of the webelement as an argument to this method in the form of string.
# It'll return the value of the given attribute name in the form of string.
# If the given attribute name doesn't have any value, it'll return none.
# It's used to verify the attribute values of the webelement like a verifying tooltip text, alternative text,
# placeholder value and the textfield is empty or not.
# The return type of this method is String.

# print(driver.find_element('id', 'prompt').get_attribute('value'))

# 6) is_displayed():
# It's used to verify that the target webelement is visible.
# The return type of this method is boolean.
# It can be used to verify whether the element is present in the DOM (Document Object Model) and also visible in the webpage.

# print(driver.find_element('xpath', '//input[@title = "search"]').is_displayed())  # True
# print(driver.find_element('id', 'hbutton').is_displayed())  # False

# 7) is_enabled():
# It's used to verify whether the target webelement is enabled or not.
# The return type of this method is boolean.
# We've to use this method upon button and input tag.

# print(driver.find_element('id', 'but2').is_enabled())  # True
# print(driver.find_element('id','tb2').is_enabled())   # False

# 8) is_selected()
# It's used to check the status of the radio button, checkbox whether it's selected or not.
# The return type of this method is boolean.
# We can use this method only on checkbox, radio button and drop-down.

# print(driver.find_element('id', 'checkbox1').is_selected())  # True
# print(driver.find_element('id', 'checkbox2').is_selected())  # False

# 9) location:
# It's a property that is used to get x, y position/ co-ordinates of the target webelement.
# It'll return the co-ordinates in a key-value pair.
# The return type of this property is dictionary.

# print(driver.find_element('link text', 'SeleniumTutorial').location)

# 10) location_once_scrolled_into_view:
# This property will get the element to be scrolled into the view.
# It's used to scroll where the element is located on the screen.
# It'll return the top lefthand corner location on the screen, or zero coordinates if the element is not visible.
# The return type of this property is dictionary.

# print(driver.find_element('id', 'radio1').location_once_scrolled_into_view)

# 11) rect:
# It's used to get both the size and the location of the target webelement.
# It'll return the x, y coordinates as well as the height and the width of the target webelement in a key-value pair.
# The return type of this property is dictionary.

# print(driver.find_element('link text', 'SeleniumTutorial').rect)

# 12) screenshot():
# We've to pass file path with a file name and file type as an argument.
# It'll take the screenshot of the webelement based on the target type specified as an argument.
# It'll save the screenshot as a file (.png).
# To get a unique screenshot, we've to change the file name frequently, or we can concatenate the file name with
# system date and time.
# It'll take the screenshots in other formats such as jpg, jpeg, but png is recommended as it shows a warning like
# 'name used for saved screenshot does not match a file type. It should end with a `.png` extension.'
# # The return type of this method is boolean.

# driver.find_element('link text', 'SeleniumTutorial').screenshot(r'D:\Programming\Python\PythonSelenium\screenshots\Screenshot_img.png')

# 13) send_keys():
# It's used to enter the data into the textfield by passing the data as an argument.
# We can also perform keyboard simulation with the help of a class called Keys.
# Keys class has a set of special key functions by this we can perform the keyboard simulation.
# It's also used to upload a file by passing the file path as an argument.
# The arguments like keys, filepath, single and multiple text can be passed as an argument to this method.
# The return type of this method is none.

# text_area = driver.find_element('id', 'ta1')
# text_area.send_keys('Surya')
# text_area.send_keys(Keys.CONTROL+'A', Keys.BACK_SPACE)

# file_upload = driver.find_element('id', 'uploadfile')
# file_upload.location_once_scrolled_into_view
# file_upload.send_keys(r'D:\Programming\Python\PythonSelenium\screenshots\Screenshot_img.png')

# 14) size
# It's used to get height and width of the target webelement.
# It'll return the size in a key-value pair.
# The return type of this method is Dictionaray.

# print(driver.find_element('id', 'uploadfile').size)

# 15) submit():
# It's used to submit a form after sending the data to form, and it'll wait until the form is submitted.
# It has certain condition to perform the action that the webelement should be within the form tag.
# It's used to click on only a submit type of button which is nested within form.
# If it's used upon webelement which is not within the form tag it'll throw an exception called WebDriverException.
# And gives a warning message: To submit an element, it must be nested inside a form element.
# The return type of this method is none.

# submit_button = driver.find_element('xpath', '//button[contains(text(), "LogIn")]')
# submit_button.location_once_scrolled_into_view
# submit_button.submit()

# 16) tagname:
# It's used to get the tagname of the target webelement.
# It returns the tagname in the form of string.
# It's used to verify the tagname of the target webelement and perform the desired task.
# The return type of this property is string.

# print(driver.find_element('class name', 'dropbtn').tag_name)

# 17) text:
# It's used to get the tagtext of the target webelement.
# It's used to verify the text of the target webelement.
# It returns the text in the form of string.
# The return type of this property is string.

# print(driver.find_element('class name', 'dropbtn').text)

# 18) value_of_css_property():
# We've to pass the property name of the webelement as an argument to this method in the form of string.
# It'll return the value of the given property name in the form of string.
# If the given property name doesn't have any value, it'll return none.
# It's used to verify the styling information of the webelement like background-color, color, font-family etc...
# We can verify the color of a webelement by this method and then pass color-related styles as an argument to it.
# This returns the color in rgba/ rgb format.
# Next, we have to use the color class to convert the rgba/ rgb format to Hex code.
# The return type of this method is string.

# print(driver.find_element('class name', 'dropbtn').value_of_css_property('color'))
# element = driver.find_element('class name', 'dropbtn')
# rgba_code = element.value_of_css_property('color')
# hex_code = Color.from_string(rgba_code).hex
# rgb_code = Color.from_string(hex_code).rgb
# print(rgba_code, rgb_code, hex_code, sep='\n')

driver.minimize_window()
driver.quit()
"""
