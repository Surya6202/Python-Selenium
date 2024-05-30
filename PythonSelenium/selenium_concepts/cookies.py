"""
from selenium import webdriver
from utilities import chrome_options

driver = webdriver.Chrome(options=chrome_options)

# Cookies:
# A cookie is a small piece of data that is sent from a website and stored in your computer.
# Cookies are mostly used to recognize the user and load the stored information.
# Webdriver provides different methods to interact with cookies and the methods are:
# 1) add_cookie()
# 2) get_cookie()
# 3) get_cookies()
# 4) delete_cookie()
# 5) delete_all_cookies()

driver.get('https://www.zee5.com/')

# 1) add_cookie():
# This method will add a cookie for the current session.
# And we'have to pass cookie data in the form of dictionary.

# cookie = {"name": "serial", "value": "Srirasthu_Subhamasthu"}
# driver.add_cookie(cookie)

# 2) get_cookie():
# This method is used to get a single cookie from the current session.
# We've to pass cookie name as an argument in the form of string.
# It'll return the cookie in a set of dictonaries.
# If the given cookie name is not present the current session, it'll return None.

# print(driver.get_cookie('serial'))

# 3) get_cookies():
# This method will return a set of dictionaries, corresponding to cookies present in the current session.
# It'll return both default and user-added cookies.

# driver.get('https://www.zee5.com/')
# cookies = driver.get_cookies()
# for i in cookies:
#     print(i)

# 4) delete_cookie():
# This method is used to delete a singel cookie in the current session.
# We've to pass cookie name as an argument in the form of string.
# If the given cookie name is not there in the session, it'll just ignore it.

# driver.delete_cookie('serial')
# print(driver.get_cookie('serial'))

# 5) delete_all_cookies():
# This method is used to delete all the added cookies in the current session.
# It won't delete the default cookies present in the current session.

# driver.delete_all_cookies()

# cookies = driver.get_cookies()
# for i in cookies:
#     print(i)


driver.minimize_window()
driver.quit()
"""
