"""
import json
from configparser import ConfigParser
import openpyxl
from openpyxl import Workbook

from selenium import webdriver
from utilities import chrome_options

driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(20)

# Data-Driven Framework:
# Read the data from external resource & run the test is called Data driven testing (parameterization).
# As per the rule of the automation data shouldn’t not hardcoded(fixed) with in a test scripts, because
# data modification & maintenance is tedious job when you want to run the test with different data, instead we
# should get the data from external resource like configuration file, excel file, json file, properties file,
# db, XML, CMD Line Data.

# Advantages:
# * Maintenance of the test data is easy.
# * Modification of the test data in external recourse is easy.
# * Cross browser /platform testing is easy (means change the browser in property File).
# * Running test scripts in different Environment is easy.
# * Running test scripts in different credentials is easy.
# * We can create the test data prior the Suite execution (we can also get the data from testData team).
# * Rerunning same test Script with multiple time with different data is easy.

# 1) Configuration file:
# It's an essential part of managing project settings and parameters.
# They offer a flexible and convenient way to store and retrieve the data.
# In Python, the `configparser` module provides a powerful solution for working with configuration files.
# The file extension for configuration file is '.ini'.
# consists of sections, each led by a [section] header, followed by key/value entries separated by a specific string.
# By default, section names are case sensitive but keys/ options/ names and values are not.

# Inserting the data into configuration file:
# Import the class ConfigParser from the ConfigParser package.
# Then, Create an instance for ConfigParser.
# Upon ConfigParser reference, We should call add_section method to add the section in the form of string.
# Upon that reference, We should call set method to add the data where we should pass the added section name,
# key/ option and value as arguments in the form of string.
# Then we have to write them in the file.

# file = ConfigParser()
# header = 'Swag Labs'
# file.add_section(header)
# file.set(header, 'browser', 'chrome')
# file.set(header, 'url', 'https://www.saucedemo.com/v1/')
# file.set(header, 'username', 'standard_user')
# file.set(header, 'password', 'secret_sauce')
#
# with open(r'../files/test_data.ini', 'w') as testdata:
#     file.write(testdata)

# Reading the data from configuration file:
# Import the class ConfigParser from the ConfigParser package.
# Then, Create an instance for ConfigParser.
# Create an instance for ConfigParser.
# Upon ConfigParser reference, we should call read method to read the file where we should pass filepath as an argument
# in the form of string.
# Upon that reference, we should call get method to retrieve the data by passing the section name and key as arguments
# in the form of string.

# file = ConfigParser()
# file.read(r'../files/test_data.ini')
# print(file.get('Swag Labs', 'browser'))

# Sample program:
# def config_data(section: str, option: str):
#     file = ConfigParser()
#     file.read('../files/test_data.ini')
#     return file.get(section, option)
#
#
# header = 'Swag Labs'
# driver.get(config_data(header, 'url'))
# driver.find_element('id', 'user-name').send_keys(config_data(header, 'username'))
# driver.find_element('id', 'password').send_keys(config_data(header, 'password'))
# driver.find_element('id', 'login-button').click()

# 2) Excel file:
# Excel is a spreadsheet program in the Microsoft Office system.
# You can use Excel to create and format workbooks (a collection of spreadsheets) to analyze the data.
# Excel in Selenium is one of the most used combinations for storing test data and then running the same test case
# against various data sets.
# In python, We've many libraries to read or write the data in excel file but openpyxl is the most used libraries to
access the excel file.
# With the help of pip command, 'pip install openpyxl'.

# Writing the data into the excel file:
# 1) Inserting the data to the exsisting workbook:
# We should import openpyxl package.
# Upon that package we should call a function, load_workbook which opens the given file and returns the workbook,
# We should pass filename as an argument in the form of string.
# Then we've to specify the sheet name of the workbook.
# Upon the specified workbook, We should call cell method which returns cell object we should pass row and column
# value as arguments in the form of integer and data value in the form string or any value.
# Upon workbook reference, We should call save method and pass filepath and filename with file extension
# as an argument in the form of string.

# workbook = openpyxl.load_workbook(r'../files/Book1.xlsx')
# workbook['Info'].cell(row=6, column=1, value='Pallavi')
# workbook['Info'].cell(row=6, column=2, value='Tirupati')
# workbook['Info'].cell(row=6, column=3, value=17)
# workbook.save(r'../files/Book1.xlsx')

# 2) Creating a new workbook and inserting the data:
# Import the Workbook class from openpyxl package.
# Create an instance for Workbook class.
# upon that reference, We should call active and store it in a sheet reference.
# Upon sheet reference we should mention cell reference within the square braces and call a value property
# and intialize it with the data.
# Upon workbook reference, We should call save method and pass filepath and filename with file extension
# as an argument in the form of string.

# workbook = Workbook()
# workbook['Sheet'].title = 'Sheet1'
# sheet1 = workbook.active
# sheet1['a1'].value = 'browsers'
# sheet1['b1'].value = 'chrome'
# sheet1['c1'].value = 'edge'
# sheet1['d1'].value = 'firefox'
# sheet1['a2'].value = 'url'
# sheet1['b2'].value = 'https://www.facebook.com/'
# sheet1['c2'].value = 'https://www.saucedemo.com/v1/'
# sheet1['a3'].value = 'username'
# sheet1['b3'].value = 'surya123@gmail.com'
# sheet1['c3'].value = 'standard_user'
# sheet1['a4'].value = 'password'
# sheet1['b4'].value = 'surya@123'
# sheet1['c4'].value = 'secret_sauce'
# workbook.save(r'../files/test_data.xlsx')

# Reading the data from the excel file:
# We should import openpyxl package.
# Upon that package we should call a function, load_workbook which opens the given file and returns the workbook,
# We should pass filename as an argument in the form of string.
# Then we've to specify the sheet name of the workbook.
# Upon the specified workbook, We should call cell method which returns cell object we should pass row and column
# value as arguments in the form of integer.
# Then upon that cell object we should convert it to cell value for that we've a property called value which is
# convert the object into value and the return type of this property is any kind of data.

# data = openpyxl.load_workbook(r'../files/test_data.xlsx')['Sheet1'].cell(2, 2).value
# print(data)

# Practice:
# workbook = openpyxl.load_workbook(r'../files/Book1.xlsx')

# To print the sheet names in the excel file:
# print(workbook.sheetnames)  # ['Info', 'Product', 'Student', 'Sheet1']

# To print the active sheet:
# print(workbook.active.title)  # Info

# To print the data present in the cell by passing cell reference:
# print(workbook['Info']['A4'].value)  # Rajanandini

# To print the cell data using row and column number:
# data = workbook['Info'].cell(row=2, column=1).value  # <Cell 'Info'.A2>
# print(data)

# print(workbook['Product'].cell(row=4, column=3).value)

# rows = workbook['Info'].max_row
# columns = workbook['Info'].max_column
# print(f'The number of rows is {rows} and the columns is {columns}')

# To print all the cells in the sheet
# def excelsheet_data(sheet_name: str, row_range, column_range):
#     for row in range(2, row_range + 1):
#         for column in range(1, column_range + 1):
#             print(workbook[sheet_name].cell(row, column).value, end=' ')
#         print()
#     print()
#
#
# excelsheet_data(sheet_name='Info', row_range=5, column_range=3)
# excelsheet_data(sheet_name='Product', row_range=4, column_range=3)
# excelsheet_data(sheet_name='Student', row_range=4, column_range=2)

# Sample program:
# def excel_data(sheet_name: str, row_num: int, column_num: int):
#     data = openpyxl.load_workbook(r'../files/test_data.xlsx')[sheet_name].cell(row_num, column_num).value
#     return data
#
#
# driver.get(excel_data('Sheet1', 2, 2))
# driver.find_element('id', 'email').send_keys(excel_data('Sheet1', 3, 2))
# driver.find_element('id', 'pass').send_keys(excel_data('Sheet1', 4, 2))
# driver.find_element('name', 'login').submit()

# 3) JSON file:
# JSON is an open standard file format and data interchange format that uses human-readable text to store and
# transmit data objects consisting of attribute/ key–value pairs and arrays.
# JSON stands for 'JavaScript Object Notation' which is a text format for storing and transporting data and it's
# 'self-describing' and easy to understand.
# The file extension for this is 'filename.json'.

# Writing the data into the JSON file:
# We should store the data in the form of dict[str, str] object.
# Upon json module we should call a function called dumps and we should pass the dict object and indentation space.
# then we should create a file and write the data with the help of an abstract method called write method.

# data = {'browser': 'chrome', 'url': 'https://www.saucedemo.com/v1/', 'username': 'standard_user', 'password': 'secret_sauce'}
# json_file = json.dumps(data, indent=1)
#
# with open(r'../files/test_data.json', 'w') as file:
#     file.write(json_file)

# Reading the data from the json file:
# We should open the json file and store that in a reference.
# then, We should import json package.
# Upon json module we should call a function, loads which accepts file name as a parameter in the form of string.
# upon that reference we should pass key within the square braces in the form of string which will return
# the value in the form of string.

# file = open(r'../files/test_data.json').read()
# print(json.loads(file)['username'])  # standard_user

# Sample program:
# def json_data(key: str):
#     file = open(r'../files/test_data.json').read()
#     return json.loads(file)[key]
#
#
# driver.get(json_data('url'))
# driver.find_element('id', 'user-name').send_keys(json_data('username'))
# driver.find_element('id', 'password').send_keys(json_data('password'))
# driver.find_element('id', 'login-button').click()

driver.quit()
"""
