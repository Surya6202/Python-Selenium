"""
from selenium import webdriver
from utilities import chrome_options

driver = webdriver.Chrome(options=chrome_options)

# Webelements are the elements that are present in the webpage.
# It can be a textfield, button, link, drop-down etc...

# To find the webelements we need locators to get it we need to inspect on the target webelement.
# To inspect a webpage, We've different ways to do it:
# 1) Right click on the target element and click on inspect option then click on elements tab.
# 2) Click on three-dots menu which is on the top right window then click on more tools and then click on
# developer tools.
# 3) There's a shortcut to inspect the webpage, press 'ctrl+shift+i'.

# To find this element, we've two functions:
# 1) find_element().
# 2) find_element().

# find_element() which finds an element in webpage which accepts By strategy and locator as an argument.
# It'll start searching the element in the html document from beginning to end until the target element is found.
# Syntax: driver.find_element('locator_name', 'locator_value')
# If the element is found, it'll return the webelement where we can perform further actions on it.
# If the element is not found, it'll end up with an exception called 'NoSuchElementException'.
# If the given locator identifies multiple elements, it'll return the first matching element.

# find_elements() which finds multiple elements in webpage, which accepts By strategy and locator as an argument.
# Stores all the matching webelements inside the list collection.
# Syntax: driver.find_elements('locator_name', 'locator_value')
# If the given locator strategy is not locating any webelement, then it returns an empty list.
# It can be used to verify the total number of websites present in the webpage.
# It can be used to handle the auto-suggestions.

# Locators:
# Locators are the search criteria through which we can locate the webelements in the webpage, and it's also called as Selectors.
# By is a class which contains a set of supported locator strategies that are used to locate the webelement.
# Selenium provides eight locator strategies to locate the webelement and they' re:
# 1) id.
# 2) name.
# 3) class name.
# 4) tag name.
# 5) link text.
# 6) partial link text.
# 7) css selector.
# 8) xpath.

# Here id, name, class are the attribute names in the source code of any webelement.
# Here, the css selector and xpath are the expressions to locate webelement when other locators aren't working.
# Generally class name and tag name are used to identify multiple elements because of this, there are chances
# of getting more duplicates.

# 1) id:
# It's the primary attribute in the html document which will act as the most dominant and simple reference to identify the element.
# It cannot be used if it's not there in the source code/ associated element tag.
# It cannot be used if the value is dynamic that keeps on changing when we refresh the application webpage.

# driver.get('https://www.saucedemo.com')
# driver.find_element('id', 'user-name').send_keys('standard_user')
# driver.find_element('id', 'password').send_keys('secret_sauce')
# driver.find_element('id', 'login-button').submit()

# 2) name:
# It's the second most important attribute which works similar to the id.
# It cannot be if it's not there in the source code/ associated element tag.

# driver.get('https://www.saucedemo.com')
# driver.find_element('name', 'user-name').send_keys('standard_user')
# driver.find_element('name', 'password').send_keys('secret_sauce')
# driver.find_element('name', 'login-button').submit()

# 3) class name:
# It's used to identify the multiple elements.
# If there are any spaces in between the class attribute value, we'll end up with NoSuchElementException.
# To handle this exception, we need to replace the space with dot.
# Whenever we have the same locator name and locator value for different elements, it will always consider the first match and
# perform the certain action.
# Here indexing is not possible.

# driver.get('https://www.saucedemo.com')
# driver.find_element('class name', 'input_error.form_input').send_keys('standard_user')
# driver.find_element('class name', 'input_error.form_input').send_keys('secret_sauce')

# 4) tag name:
# It's used to identify the multiple elements.
# Here we'll get all the matching tags.
# Here indexing is not possible.

# driver.get(r'D:\Programming\PythonProgramming\PythonSelenium\files\Demo.html')
# driver.find_element('tag name', 'input').send_keys('Surya123@gmail.com')

# 5) link text:
# This is a text that is associated with the anchor tag.

# driver.get('https://www.facebook.com/')
# driver.find_element('link text', 'Forgotten password?').click()

# 6) partial link text:
# If the link text is very lengthy and partially dynamic, then we'll go for it.
# We can pass complete link text/ partial link text as an argument to find_element method.

# driver.get('https://www.facebook.com/')
# driver.find_element('partial link text', 'Forgotten').click()

# note:
# Any text enclosed within the open and close tag, it's a tag text.
# Any text that is associated with anchor tag, it's a link text.
# Any text that is not associated with anchor tag, it's a normal text.

# 7) css selector:
# CSS stands for Cascading Style Sheets, which is a language used to apply stylings to the webelement.
# Whenever we have the attributes which are not the locators, and we don't have any link text.
# We go for css selector to locate the webelement.
# Syntax: tagName[attributeName = attributValue]

# Advantages:
# It'll identify the target element faster comparing to xpath.

# Disadvantages:
# 1. Indexing is not possible (If we are having multiple matches, css selector can only locate the first match)
# 2. It does not support text functions (Since css selector takes attribute name and attribute value, it cannot locate any text)
# 3. We cannot perform backward traversing using it.

# driver.get('https://www.facebook.com/')
# driver.find_element('css selector', 'input[id="email"]').send_keys('suryar123@gmail.com')
# driver.find_element('css selector', '#pass').send_keys('surya@123')
# driver.find_element('css selector', 'button[name = "login"]').submit()

# 8) xpath:
# Xpath is the most powerful locator which is able to loate any type of the UI element.
# xpath stands for an XML path and XML stands for Extensible Markup Language.
# XML is similar to HTML, but it's used as a standard format for data exchange between a client and server.
# Using Xpath, we can traverse/ navigate through the HTML document and locate the desired element.
# Whenever we don't have locator attributes but text, we go for xpath expression.
# If the element is completely dynamic/ duplicate, we go for xpath expression.

# Note:
# If the xpath expression matches multiple elements, then the xpath will be stored those UI elements in an array.
# In this xpath array, the index starts from 1.

# Xpath is classified into two types:
# 1) Absolute Xpath.
# 2) Relative Xpath.

# 8.1) Absolute Xpath:
# It's a complete xpath expression starts from the root element to the target element and used to locate the UI/ web elements.
# Here, we've two symbols: '.' denotes the current document and '/' denotes the immediate child tag of the parent tag.
# Example: ./html/body/form/input or html/body/form/input

# Advantages:
# It locates the UI elements faster, as they contain the complete path of the UI element from the root.

# Disadvantages:
# It's very lengthy and time-consuming.
# Due to changes in a UI element like position, the xpath expression may change and won't work.

# To overcome the absolute xpath drawbacks, we're going for relative xpath and before moving to relative xpath, we
# should be good in absolute xpath.

# driver.get('https://www.facebook.com/')
# driver.find_element('xpath', 'html/body/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/form/div[2]/button').submit()

# 8.2) Relative Xpath:
# It's a direct/ shorcut path that will start from the root element and used for locating the web elements.
# Here, Relative xpath starts with a double slash symbol '//' denotes the child of any parent or any child.
# Example: //input
# Comparing to absolute xpath, Relative xpath is shorter.
# Relative xpath is classified into five types:
# 1) Xpath by attributes.
# 2) Xpath by functionns.
#    2.1) Xpath by text()
#    2.2) Xpath by contains()
# 3) Xpath by index.
# 4) Independent and Dependent Xpath.
# 5) Xpath by axes.

# 8.2.1) Xpath by attribute:
# The process of deriving the address of the webelement by using its attribute name and value.
# Here, with the help of webelement attribute name and value, we'll derive an expression.
# Syntax: //tag_name[@attribute_name = "attribute_value"]
# Here '@' symbol denotes that it's used to access the attribute.
# tag_name denotes a particular tag, to access all tags we can use wild card symbol '*'.
# Example:
# //input[@id = "email"] - particular tag depends on attribute value.
# //*[@id = "pass"] - all tags depend on attribute value.
# //input[@id = "email" and @name = "email"]/ //input[@id = "email" or @name = "email"] - using logical operations
# If attribute name and value are lengthy, partial and dynamic, or if the tag doesn't have attributes, we can't use this expression.

# driver.get('https://www.facebook.com/')
# driver.find_element('xpath', '//input[@id = "email"]').send_keys('9876543210')
# driver.find_element('xpath', '//*[@name = "login"]').submit()

# 8.2.2) Xpath by functions:
# Based on certain functions, this xpath is further classified into types:
# 1) Xpath by text():
# The process of deriving the address of the webelement by using its tag text.
# Here, with the help of webelement tag text, we'll derive an expression.
# Syntax: //tag_name[text(), "tag_text"]
# If we don't have any attributes but only tag text, we go for this xpath expressin.
# By using this expression, we can identify both link and normal text.
# If the tag text is lengthy, partial and dynamic, we should not use this expression.

# driver.get('https://www.facebook.com/')
# driver.find_element('xpath', '//button[text()= "Log in"]').submit()

# 2) Xpath by contains():
# The process of deriving the address of the webelement by using attribute name and value and tag text.
# Syntax: //tag_name[contains(@attribute_name/ text(), "attribute_value"/ "tag_text" )]
# We can locate the webelement by this expression in 2 types
# 2.1) Xpath by partial attribute:
# syntax: //tag_name[contains(@attribute_name, "attribute_value" )]
# Whenever the attribute name and value are lengthy and partially dynamic, we go for this expression.

# driver.get('https://www.facebook.com/')
# driver.find_element('xpath', '//input[contains(@data-testid,"email")]').send_keys('9876543210')

# 2.2) Xpath by partial text:
# syntax: //tag_name[contains(text(), "tag_text" )]
# Whenever the tag text is lengthy and partially dynamic, we go for this expression.

# driver.get('https://www.facebook.com/')
# driver.find_element('xpath', '//a[contains(text(), "account")]').click()

# 8.2.3)Xpath by index:
# The process of deriving the address of the webelement by indexing among the group of elements.
# To identify the unique element among the group of duplicates using indexing.
# Syntax: (Xpath by attribute, functions and axes)[index_number]
# Whenever the xpath for fixed element itself is duplicate in such cases, we go for this expression.
# Whenever there's no way to identify the element uniquely using other xpath, we go for this expression.

# driver.get('https://www.facebook.com/')
# driver.find_element('xpath', '(//input)[4]').send_keys('surya123')

# 8.2.4) Independent and Dependent Xpath:
# It's a process of locating a completely dynamic/ duplic element using another type of xpath and also by
# backward traversing.
# Here independent means a static element and dependent means a dynamic element.
# If the static element itself is dynamic, we should not go for independent and dependent xpath.

# Steps to write independent and dependent xpath:
# step 1: Identify the scenario.
# step 2: Identify which element is static and which element is dynamic.
# step 3: Derive the xpath expression to identify a static element.
# step 4: Modify the xpath to identify immediate common parent by performing backward traversing.
# step 5: Modify the xpath by deriving xpath expression for a dynamic element.

# note:
# '/' denotes forward traversing or identifying immediate child.
# '/..' denotes backward traversing or identifying immediate parent.

# driver.get('https://www.amazon.in/')
# driver.find_element('id', 'twotabsearchtextbox').send_keys('python book for beginners')
# driver.find_element('xpath', '//input[contains(@id,"nav-search")]').click()
# driver.find_element('xpath', '(//a[text()="Paperback"])[2]').click()
# price_details = driver.find_element('xpath', '//span[@id="productTitle"]/../../../../..//span[@id="price"]')
# print(price_details.text)

# 8.2.5) Xpath by axes:
# It represents the relationship between current element and the set of relative element.
# It's used to locate an element that is relative to the current element.
# It's used to identify a completely dynamic/ duplicate element based on the relationship.
# Here, we can use various traversings in a simple way by using different axis names.
# Syntax: //static_element_xpath/axis_name::tag_name[predicate/ condition]xpath
# The following are the different types of axis names:
# parent, child, following, preceding, following-sibling, preceding-sibling, descendant, ancestor.

# Based on traversing, it's classified into
# forward axes: child, following, following-sibling, descendant.
# backward axes: parent, preceding, preceding-sibling, ancestor.

# 1) Child:
# It'll select all the child of the current element

# 2) following:
# It'll select all the following elements of the current element.

# 3) following-sibling:
# It'll select the following sibling elements of the current element.

# 4) Descendant:
# It'll select all the direct descendants (child, grandchild...) of the current element.

# 5) Parent:
# It'll select the parent of the current element.

# 6) Preceding:
# It'll select all the preceding elements of the current element.

# 7) Preceding-sibling:
# It'll select the preceding-sibling elements of the current element.

# 8) Ancestor:
# It'll select all the ancestors (parent, grandparent...) of the current element.

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

# driver.get('https://omayo.blogspot.com/')
# driver.implicitly_wait(20)
# links = driver.find_elements('xpath', '//div[@id = "LinkList1"]/descendant::a')
# for link in links:
#     link.click()
#     driver.back()

driver.minimize_window()
driver.quit()
"""
