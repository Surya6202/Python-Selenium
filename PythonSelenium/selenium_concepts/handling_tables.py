"""
from time import sleep

from selenium import webdriver

from utilities import chrome_options

driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(30)

# Web tables:
# They're like normal tables where the data is presented in a structured form using rows and columns.
# The only difference is that they are displayed on the web with the help of HTML code.
# The tag <table> is the HTML tag used to define a web table.
# While <th> is used for defining the header of the table, <tr> and <td> tags are used for defining rows and columns
# respectively for the web table.

# Types of tables:
# Depending on the data in the table, web tables can be classified as Static web tables and Dynamic web tables.

# 1. Static Web Tables
# These tables have fixed data that remains unchanged throughout.
# Due to the static nature of their content, they are called Static web tables.

# Retrieve the headings from the table:
# driver.get(r'D:\Programming\Python\PythonSelenium\files\Demo.html')
# for heading in driver.find_elements('tag name', 'th'):
#     print(heading.text, end=' ')
# print()

# Retrieve all the data from the table:
# driver.get(r'D:\Programming\Python\PythonSelenium\files\Demo.html')
# for data in driver.find_elements('tag name', 'td'):
#     print(data.text)

# Retrieving the data from first row:
# driver.get(r'D:\Programming\Python\PythonSelenium\files\Demo.html')
# for j in driver.find_elements('xpath', '//tr[@row= "1"]/td'):
#     print(j.text, end=' ')
# print()

# Retrieving the data from two row:
# driver.get(r'D:\Programming\Python\PythonSelenium\files\Demo.html')
# for j in driver.find_elements('xpath', '//tr[@row= "2"]/td'):
#     print(j.text, end=' ')
# print()

# Retrieving the data from third row:
# driver.get(r'D:\Programming\Python\PythonSelenium\files\Demo.html')
# for j in driver.find_elements('xpath', '//tr[@row= "3"]/td'):
#     print(j.text, end=' ')
# print()

# To print the entire table:
# driver.get(r'D:\Programming\Python\PythonSelenium\files\Demo.html')
# rows = driver.find_elements('xpath', '//tbody/tr')
# for heading in driver.find_elements('tag name', 'th'):
#     print(heading.text, end=' ')
# print()
# for i in range(1, len(rows)+1):
#     for j in driver.find_elements('xpath', f'//tr[@row= "{i}"]/td'):
#         print(j.text, end=' ')
#     print()

# driver.get(r'D:\Programming\Python\PythonSelenium\files\Demo.html')
# rows = len(driver.find_elements('tag name', 'th'))+2
# columns = len(driver.find_elements('xpath', '//tbody/tr'))+1
# for r in range(1, rows):
#     for c in range(1, columns):
#         if r == 1:
#             print(driver.find_element('xpath', f'//th[{str(c)}]').text, end=' ')
#         else:
#             print(driver.find_element('xpath', f'//tbody/tr[{str(r-1)}]/td[{c}]').text, end=' ')
#     print()

# To find number of rows and columns of the table:
# driver.get(r'D:\Programming\Python\PythonSelenium\files\Demo.html')
# rows = driver.find_elements('tag name', 'th')
# columns = driver.find_elements('xpath', '//tbody/tr')
# print(f'The table has {len(rows)} rows and {len(columns)} columns.')

# 2. Dynamic Web Tables:
# These tables have data that changes over time, and hence the number of rows and columns might also change depending
# upon the data shifts.
# Due to the dynamic nature of their content, they are called Dynamic web tables.
# Often, the functionalities of web applications depend on the data carried by Dynamic web tables, as they act as the
# data source for the functional modules in many cases.

# Retrieve the headings from the table
# driver.get('https://seleniumpractise.blogspot.com/')
# for heading in driver.find_elements('xpath', '//table[@id = "customers"]/descendant::th'):
#     print(heading.text, end=' ')
# print()

# Retrieve all the data from the table:
# driver.get('https://seleniumpractise.blogspot.com/')
# for data in driver.find_elements('xpath', '//table[@id = "customers"]/descendant::td'):
#     print(data.text)

# To print the entire table:
# driver.get('https://seleniumpractise.blogspot.com/')
# for heading in driver.find_elements('xpath', '//table[@id = "customers"]/descendant::th'):
#     print(heading.text, end=' ')
# print()
# columns = driver.find_elements('xpath', '//table[@id = "customers"]/descendant::th')
# for i in range(2, len(columns)+2):
#     for j in driver.find_elements('xpath', f'//table[@id = "customers"]//tr[{str(i)}]/td'):
#         print(j.text, end=' ')
#     print()

# driver.get('https://python.org/')
# driver.find_element('xpath', '(//a[text()="Downloads"])[1]').click()
# driver.find_element('xpath', '//a[text()="PythonProgramming 3.8.18"]/../..//span[@class="release-enhancements"]').click()

# driver.get('https://www.nseindia.com/')
# element = driver.find_element('xpath', '//a[text()="BPCL"]/../..//td[contains(@class,"greenTxt")]')
# element.location_once_scrolled_into_view
# print(element.text)

driver.quit()
"""