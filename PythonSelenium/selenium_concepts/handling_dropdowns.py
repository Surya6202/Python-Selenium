"""
from selenium import webdriver
from selenium.webdriver.support import select
from utilities import chrome_options

driver = webdriver.Chrome(options=chrome_options)

# Drop-downs:
# Drop-down is another major component of the webpage that enables user to choose the option among the given
# list of options.
# Generally drop-down is of four types:
# 1) Single-select drop-down.
# 2) Multi-select drop-down.
# 3) Bootstrap drop-down.
# 4) JQuery drop-down.

# In Selenium, the Select class provides the implementation of the HTML 'select' tag.
# A select tag provides the helper methods with select and deselect options.
# This select class is used to select one of the options in a drop-down box or an option among multiple selection boxes.
# To access it, we've to create an object, and with that object reference we can select the option.
# We've to pass webelement as an argument and that element tag should be of Select tag if anyother than select tag
# it'll throw 'UnexpectedTagNameException'.
# Syntax: var_name = Select(web_element)
# Select class has certain methods through which we're going to select the options in the drop-down/ get the
# options from the drop-down.

# 1) all_selected_options:
# It's used to get all selected options in the drop-down and returns the selected options in the form of list<webelement>.
# It supports both single and multi-select drop-down.

# 2) deselect_all():
# It's used to deselect all the selected options in a drop-down at a time.
# This will be valid only the drop-down supports multi selections.
# If the drop-down does not support multiple selections, it'll throw 'NotImplementedError'.

# 3) deselect_by_index():
# It's used to deselect the selected options in the drop-down by passing the index value of the options in the form of integer.
# If the given arguments are not matching, we'll get an exception called 'NoSuchElementException'.
# If the drop-down does not support multiple selections, it'll throw 'NotImplementedError'.

# 4) deselect_by_value:
# It's used to deselect the selected options in the drop-down by passing the value of value attribute as an argument in the form
# of string.
# If the given arguments are not matching, we'll get an exception called 'NoSuchElementException'.
# If the drop-down does not support multiple selections, it'll throw 'NotImplementedError'.

# 5) deselect_by_visible_text():
# It's used to deselect the selected options in the drop-down by passing the visible text as an argument in the form of string.
# If the given arguments are not matching, we'll get an exception called 'NoSuchElementException'.
# If the drop-down does not support multiple selections, it'll throw 'NotImplementedError'.

# 6) first_selected_option:
# It's used to get the first/ default selected option in the drop-down and returns default selected option in the form of webelement.
# It's most essential while checking the default selected option in the dropdown since it's directly synchronized with local system
# date and time.
# It supports both single and multi-select drop-down.
# If no options are selected, we'll end up with 'NoSuchElementException'.

# 7) is_multiple:
# It's used to check the type of the drop-down in the webpage.
# If it returns true, the drop-down is multi-select drop-down.
# If it returns none, the drop-down is single-select drop-down.

# 8) options:
# It's used to get all the options in the drop-down and returns all the options in the form of list<webelement>.
# We can use it to verify all the options in the list are correct or not and they're in proper order or not.

# 9) select_by_index():
# It's used to select the option in the drop-down by passing the index value of the option in the form of integer.

# 10) select_by_value():
# It's used to select the option in the drop-down by passing the value of value attribute as an argument in the form of string.

# 11) select_by_visible_text():
# It's used to select the option in the drop-down by passing the visible text as an argument in the form of string.

# note:
# 1) If the given arguments are not matching, we'll get an exception called 'NoSuchElementException'.
# 2) deselect_by_visible_text, by_value, All, by_index used to multi-select dropdown, if we try to use it for
# single-select drop-down, we'll get an error called 'NotImplementedError'.

# 1) Single-select drop-down:
# This type of drop-down enables user to select one option among the list.

# driver.get('https://www.globalsqa.com/demo-site/select-dropdown-menu/')
# dropdown = driver.find_element('tag name', 'select')
# select = Select(dropdown)

# elements = select.all_selected_options
# countries = []
# for element in elements:
#     countries.append(element.text)
# print(countries)  # Afghanistan

# select.deselect_all()  # NotImplementedError

# select.deselect_by_index(0)  # NotImplementedError

# select.deselect_by_value('AFG')  # NotImplementedError

# select.deselect_by_visible_text('Afghanistan')  # NotImplementedError

# print(select.first_selected_option.text) # Afghanistan

# print(select.is_multiple)  # None

# elements = select.options
# countries = []
# for element in elements:
#     countries.append(element.text)
# print(countries)  # ['Afghanistan', 'Åland Islands', 'Albania',....]

# select.select_by_index(102)  # India

# select.select_by_value('IND')  # India

# select.select_by_visible_text('India')  # India

# 2) Multi-select drop-down:
# This type of drop-down enables user to select single option, multi options or all options.

# driver.get('https://omayo.blogspot.com/')
# dropdown = driver.find_element('id', 'multiselect1')
# select = Select(dropdown)

# elements = select.all_selected_options
# cars = []
# for element in elements:
#     cars.append(element.text)
# print(cars)  # []

# for i in range(4):
#     select.select_by_index(i)
# select.deselect_all()

# for i in range(2):
#     select.select_by_index(i)
# for i in range(2):
#     select.deselect_by_index(i)

# cars = ['audix', 'volvox']
# for i in cars:
#     select.select_by_value(i)
# for i in cars:
#     select.deselect_by_value(i)

# cars = ['Volvo', 'Swift', 'Hyundai']
# for i in cars:
#     select.select_by_visible_text(i)
# for i in cars:
#     select.deselect_by_visible_text(i)

# print(select.is_multiple)  # True

# By default,
# print(select.first_selected_option.text) # NoSuchElementException("No options are selected")

# select.select_by_index(2)
# print(select.first_selected_option.text) # Hyundai

# elements = select.options
# cars = []
# for element in elements:
#     cars.append(element.text)
# print(cars)  # ['Volvo', 'Swift', 'Hyundai', 'Audi']

# 3) Bootstrap drop-down:
# Bootstrap is a popular open-source front-end web development framework that provides a set of HTML, CSS, and
# JavaScript templates.
# Bootstrap provides a set of classes and utilities to style and customize the appearance and behavior of the dropdown.
# Bootstrap Dropdown is similar to drop-down field with good appearance and customization.

# driver.get('https://www.shaadi.com/')
# driver.implicitly_wait(30)
# driver.execute_script('window.scrollBy(0, 300)')
# driver.find_element('xpath', '//div[contains(@data-testid, "gender")]/child::div').click()
# driver.find_element('xpath', '//div[contains(@data-testid, "gender")]//following::div[text()="Man"]').click()
# driver.find_element('xpath', '//div[contains(@data-testid,"age_from")]').click()
# driver.find_element('xpath', '//div[contains(@data-testid,"age_from")]/descendant::div[text() = "26"]').click()
# driver.find_element('xpath', '//div[contains(@data-testid,"age_to")]').click()
# driver.find_element('xpath', '//div[contains(@data-testid,"age_to")]/descendant::div[text() = "31"]').click()
# driver.find_element('xpath', '//label[text() = "of religion"]/../descendant::div[text() = "Select"]').click()
# driver.find_element('xpath', '//div[text() = "Select"]/following::div[text() = "Hindu"]').click()
# driver.find_element('xpath', '//label[contains(text(), "mother")]/..//div[text() = "Select"]').click()
# driver.find_element('xpath', '//div[text() = "Select"]/following::div[text() = "Frequently Used"]/'
#                              'following-sibling::div[text() = "Telugu"]').click()
# driver.find_element('xpath', '//div[contains(@data-testid,"age_from")]').click()
# driver.find_element('xpath', '//div[contains(@data-testid,"age_from")]/descendant::div[text() = "26"]').click()
# driver.find_element('xpath', '//button[text() = "Let\'s Begin"]').click()

# 4) JQuery drop-dowm:
# JQuery is a popular JavaScript library that simplifies the process of adding interactivity and dynamic effects
# to a website.
# One of the features it provides is the ability to create dropdown menus.
# A dropdown menu is a list of options that is hidden until the user clicks on a button or a link.
# When the user clicks on the button or link, the dropdown menu appears, displaying a list of options.
# The user can then select one of the options by clicking on it.

# driver.get('https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/')
# driver.implicitly_wait(20)
# driver.find_element('id', 'justAnInputBox').click()
# driver.find_element('xpath', '(//span[contains(text(),"choice 1")])[1]').click()
# driver.find_element('xpath', '(//span[contains(text(),"choice 4")])[1]').click()
# driver.find_element('xpath', '//h1[contains(text(), "Combo")]').click()
# sleep(5)

driver.quit()
"""
