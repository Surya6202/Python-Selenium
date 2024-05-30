"""
from selenium import webdriver
from selenium.webdriver import ActionChains

from utilities import chrome_options

driver = webdriver.Chrome(chrome_options)
driver.implicitly_wait(20)
actions = ActionChains(driver)

# JavaScript:
# JavaScript (JS) is a programming language used to make websites and applications dynamic and interactive.
# It’s unique because it can run directly in your browser, not just on a server.
# Along with hypertext markup language (HTML) and cascading style sheets (CSS), JavaScript is one of the most commonly
# used programming languages of the internet.

# JavaScriptExecutor:
# It helps to execute JavaScript through Selenium Webdriver.
# It provides two methods “execute_script” & “execute_async_script” to run javascript on the selected
# window or current page.
# In Selenium Webdriver, locators like XPath, CSS, etc. are used to identify and perform operations on a web page.
# In case, these locators do not work you can use JavaScriptExecutor. You can use JavaScriptExecutor to perform an
# desired operation on a web element.
# Selenium supports JavaScriptExecutor and upon driver reference we can call this two methods.

# 1) execute_script():
# This method executes JavaScript in the context of the currently selected frame or window in Selenium.
# The script used in this method runs in the body of an anonymous function (a function without a name).
# We can also pass complicated arguments to it.
# The script can return values. Data types returned are Boolean, Long, String, List, WebElement.
# Syntax:
# Upon driver reference, we can call this two methods:
# driver.execute_script(script='window.scrollBy(0, 100)',)
# Script – This is the JavaScript that needs to execute.
# Arguments – It is the arguments to the script. It’s optional.

# 2) execute_async_script():
# With Asynchronous script, your page renders more quickly.
# Instead of forcing users to wait for a script to download before the page renders.
# This function will execute an asynchronous piece of JavaScript in the context of the currently selected
# frame or window in Selenium.
# The JS so executed is single-threaded with a various callback function which runs synchronously.

# JavaScriptExecutor Commands:
# 1) Display the alert, prompt and confirmation popup:
# driver.get('https://omayo.blogspot.com')
# driver.execute_script('alert("Hello! Surya")') # alert-popup
# driver.execute_script('confirm("press OK to continue")')
# driver.execute_script('prompt("Enter your favourite person name?")')

# 2) Click on a webelement:
# We can perform it in two ways:
# 2.1) using getElementById function only if the element has a static id attribute.
# driver.get('https://omayo.blogspot.com/')
# driver.execute_script('document.getElementById("alert1").click()')

# 2.2) passing webelement as an argument:
# driver.get('https://www.facebook.com/')
# element = driver.find_element('link text', 'Forgotten password?')
# driver.execute_script('arguments[0].click()', element)

# 3) Enter the text into webelement:
# driver.get('https://www.facebook.com/')
# email_textfield = driver.find_element('id', 'email')
# driver.execute_script('arguments[0].value = "surya123@gmail.com"', email_textfield)

# 4) Flashing an element on screen:
# driver.get('https://www.facebook.com/')
# element = driver.find_element('name', 'login')
# color = element.value_of_css_property('backgroundcolor')
# colors = ['aqua', 'blue', 'fuchsia', 'grey', 'green', 'lime', 'maroon']
# for i in colors:
#     driver.execute_script(f'arguments[0].style.background="{i}"', element)
#     sleep(3)
#     driver.execute_script(f'arguments[0].style.background="{color}"', element)
#     sleep(2)

# 5) Highlighting an element with border:
# driver.get('https://www.facebook.com/')
# element = driver.find_element('id', 'email')
# for i in range(1, 6):
#     driver.execute_script(f'arguments[0].style.border="{str(i)}px solid red"', element)
#     sleep(2)


# 6) Retrieve the title of the webpage:
# driver.get('https://www.facebook.com/')
# print(driver.execute_script('return document.title'))

# 7) Retrieve the Url of the webpage:
# driver.get('https://www.facebook.com/')
# print(driver.execute_script('return document.URL'))

# 8) Navigate to the given url:
# driver.execute_script('document.location= "https://www.facebook.com"')

# 9) Selecting a date in the calendar:
# driver.get('https://seleniumpractise.blogspot.com/2016/08/how-to-handle-calendar-in-selenium.html')
# driver.execute_script(f'document.getElementById("datepicker").value="02/06/2002"')

# 10) Navigation:
# driver.get('https://www.facebook.com/')
# driver.find_element('name', 'login').submit()
# Backward:
# driver.execute_script('history.back(0)')
# Forward:
# driver.execute_script('history.forward(0)')
# driver.execute_script('history.back(0)')
# Refresh:
# driver.execute_script('history.go(0)')
# or
# driver.execute_script('location.reload(0)')

# 11) Scrolling untill the element is visible into the view:
# driver.get('https://www.facebook.com/')
# element = driver.find_element('partial link text', 'Contact')
# driver.execute_script('arguments[0].scrollIntoView(true)', element)

# 12) Scroll the webpage:
# 12.1) window.scrollBy(0, 0) - Scroll the webpage horizontally or vertically based on the parameters
# (horizontal_scroll, vertical_scroll) in numbers.
# driver.get('https://omayo.blogspot.com/')
# driver.execute_script('window.scrollBy(0, 200)')
# driver.execute_script('window.scrollBy(0, 200)')

# 12.2) window.scrollTo(0, 0) - Scroll the webpage horizontally or vertically based on the parameters
# (horizontal_scroll, vertical_scroll) in numbers.
# driver.get('https://omayo.blogspot.com/')
# driver.execute_script('window.scrollTo(0, 200)')
# driver.execute_script('window.scrollTo(0, 200)')

# Note: scrollBy will continue the scrolling from where it scrolled last whereas scrollTo will start over from initial position
# each time.

# 12.3) Scroll the webpage vertically based on the parameters and the parameters are
# (0, document.documentElement.scrollHeight), it'll scroll to the end of the page.
# driver.get('https://omayo.blogspot.com/')
# driver.execute_script('window.scrollTo(0, document.documentElement.scrollHeight)')

# 14) Retrieve the present/ entered value of the webelement:
# driver.get('https://www.facebook.com/')
# email = driver.find_element('id', 'email')
# email.send_keys('surya123@gmail.com')
# print(driver.execute_script('return arguments[0].value', email))

# 15) Retrieve the visible text of the webelement:
# driver.get('https://www.facebook.com/')
# element = driver.find_element('partial link text', 'Forgotten')
# print(driver.execute_script('return arguments[0].text', element))
# or
# print(driver.execute_script('return arguments[0].innerText', element))

# 16) Retrieve the attribute value:
# driver.get('https://www.facebook.com/')
# element = driver.find_element('id', 'email')
# print(driver.execute_script('return arguments[0].getAttribute("aria-label")', element))
# print(driver.execute_script('return arguments[0].placeholder', element))

# 17) Check element is enabled or not:
# If it returns true then the element is disabled if not the element is enabled.
# driver.get('https://omayo.blogspot.com/')
# ele1 = driver.find_element('id', 'but1')
# print(driver.execute_script('return arguments[0].disabled', ele1))
# ele2 = driver.find_element('id', 'but2')
# print(driver.execute_script('return arguments[0].disabled', ele2))

# 18) Check element is selected or not:
# If it returns true then the element is selected if not the element is deselected.
# driver.get('https://omayo.blogspot.com/')
# ele1 = driver.find_element('id', 'checkbox1')
# print(driver.execute_script('return arguments[0].checked', ele1))
# ele2 = driver.find_element('id', 'checkbox2')
# print(driver.execute_script('return arguments[0].checked', ele2))

# 19) Check element is displayed or not:
# If it returns true then the element is hidden if not the element is dispalyed.
# driver.get('https://omayo.blogspot.com/')
# ele1 = driver.find_element('id', 'hbutton')
# print(driver.execute_script('return arguments[0].hidden', ele1))
# ele2 = driver.find_element('name', 'textboxn')
# print(driver.execute_script('return arguments[0].hidden', ele2))

# 20) To block the ads:
# driver.get('https://www.globalsqa.com/demo-site/frames-and-windows/#iFrame')
# actions.pause(5).perform()
# driver.execute_script('const elements = document.getElementsByClassName("adsbygoogle adsbygoogle-noablate");'
#                       'while (elements.length > 0) elements[0].remove()')


# Sample program:
# driver.execute_script('document.location= "https://www.facebook.com"')
# driver.execute_script('arguments[0].value= "surya123@gmail.com"', driver.find_element('id', 'email'))
# driver.execute_script('arguments[0].value= "surya@123"', driver.find_element('id', 'pass'))
# driver.execute_script('arguments[0].click()', driver.find_element('name', 'login'))

driver.quit()
"""