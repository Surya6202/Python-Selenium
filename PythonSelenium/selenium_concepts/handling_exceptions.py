from time import sleep

from selenium import webdriver

from selenium.common import exceptions

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
options.add_argument('--start-maximized')

driver = webdriver.Chrome(options)

# Exception:
# In python, It's an event that disrupts the normal flow of a code.
# It'll be raised only when the program is executed.

# Exception handling:
# It's a mechanism used to handle the exception so that the code can continue it's execution.
# In selenium we've many inbuilt exceptions that'll be thrown at the code execution.

# 1) StaleElementReferenceException:
# Thrown when a reference to an element is now "stale".
# Stale means the element no longer refered by that element reference.
# Possible causes of StaleElementReferenceException :
# 1) You are no longer on the same page, or the page may have refreshed since the element was located.
# 2) The element may have been removed and re-added to the screen, since it was located, Such as an
# element being relocated.
# 3) This can happen typically with a javascript framework when values are updated and the node is rebuilt.
# This can be handled
driver.get('https://www.facebook.com/')
driver.implicitly_wait(30)
email = driver.find_element('id', 'email')
password = driver.find_element('id', 'pass')
email.send_keys('hi')
password.send_keys('hello')
driver.refresh()
email.clear()


exceptions.NoSuchFrameException

# exceptions.StaleElementReferenceException

driver.minimize_window()
driver.quit()

