"""
import warnings
from base64 import b64decode
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.remote.command import Command

from utilities import chrome_options

driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(30)

# Screenshot:
# A Screenshot in Selenium Webdriver is used for bug analysis.
# To capture entire webpage screenshots in Selenium, one has to utilize the methods save_screenshot and
# get_screenshot_as_file.
# This notifies WebDriver that it should take a screenshot in Selenium and store it in the given file path.

# Screenshot methods:
# 1) get_screenshot_as_base64() - It'll take the screenshot of the current window as a base64 encoded string which is
# useful in embedded images in HTML. This will internally execute the standard screenshot command and its value is
# returned as base64 string.

# 2) get_screenshot_as_png() - It'll take the screenshot of the current window as a binary data. This method internally
# calls the get_screenshot_as_base64() and it'll return base64 string which is encoded as ascii value and then it's
# decoded into bytes data with the help of a function b64decode(). The return type of this method is bytes.

# 3) get_screenshot_as_file() - It'll take the screenshot and saves a screenshot of the current window to a
# PNG image file. We should pass filename with filepath as an argument in the form of string. The return type of this
# method is boolean. It returns 'False' if there is any IOError, else it returns True. It internally calls
# get_screenshot_as_png() and writes the bytes data with given file name and stores  it in the specified location.
# If the path is incorrect/ any file related error it'll throw an OSError and will delete the bytes data.

# 4) save_screenshot() - It's similar to get_screenshot_as_file() and we've to pass filename and filepath as an argument
# in the form of string. It internally calls get_screenshot_as_file().

# Note:
# This all methods are inter-related to each one as each methods return one kind of data from there to we've to convert
# it to png file.
# The methods get_screenshot_as_file() and save_screenshot() will save the screenshot only if the file extension is
# 'png' if not it'll throw an warning message as "UserWarning: name used for saved screenshot does not match file type.
# It should end with a `.png` extension".
# Then it'll delete that converted bytes data automatically.
# For every time we need to change file name to get an unique screenshot, so inorder to get the screenshot we have to
# concatenate the filename with date and time.
# DateTime stamp:
date = datetime.now().strftime('%d-%m-%Y')
time = datetime.now().strftime('%H-%M-%S%f')[0:10]

# If we specify only the filename it'll save the screenshot in the same folder

# driver.get('https://www.zee5.com/')
#
# print(driver.get_screenshot_as_base64())  # 5xlsveh2nLltjpdsz/EyGNy6K3jflR............
#
# print(driver.get_screenshot_as_png())   # b4b>o\xe6\x03\xa6\xcd\xbd\x00\x12\x1ek\x15Q\........
#
# driver.get_screenshot_as_file('Webpage.png')
# driver.save_screenshot('screenshot.png')

# Internal conversion:
# driver.get('https://muffingroup.com/blog/colorful-websites/')

# Converting Standard screenshot command into base64 string:
# standard_screenshot = driver.execute(Command.SCREENSHOT)['value']
# base_64 = standard_screenshot
# print(base_64)  # 5xlsveh2nLltjpdsz/EyGNy6K3jflR............

# Converting base64 data into bytes data:
# base64_data = driver.get_screenshot_as_base64()
# bytes_data = b64decode(base64_data.encode('ascii'))
# print(bytes_data)  # b4b>o\xe6\x03\xa6\xcd\xbd\x00\x12\x1ek\x15Q\........

# Converting bytes data into img file(png, jpg, jpeg):
# png = driver.get_screenshot_as_png()
# with open(r'../screenshots/webpagescreenshot.jpg', 'wb') as f:
#     f.write(png)

# To save the screenshot in any img format we need to modify/ recreate the screenshot method and add to the package:
# def screenshot(filename: str):
#     if not (filename.lower().endswith('.png') or filename.lower().endswith('.jpeg') or filename.lower().endswith(
#             '.jpg') or
#             filename.lower().endswith('.gif')):
#         message = ('File extension mismatch.\nThe user is trying to save the screenshot file with other extension.\n'
#                    'The acceptable file extensions for screenshots are ".png", ".jpeg", ".jpg", ".gif". \n')
#         warnings.warn(message=message, category=UserWarning, stacklevel=2)
#         del filename
#         return False
#     else:
#         img_file = b64decode(driver.execute(Command.SCREENSHOT)['value'].encode('ascii'))
#         with open(filename, 'wb') as file:
#             file.write(img_file)
#         del img_file
#         return True


driver.get('https://www.instagram.com/')
username = driver.find_element('name', 'username')
username.send_keys('suryar6202')
driver.save_screenshot()
assert username.element_screenshot(r'../screenshots/webelement.jpg')
assert driver.screenshot(r'../screenshots/webpage.jpg')

driver.quit()
"""
