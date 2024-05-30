'''
Selenium Installation

Go to cmd prompt --> pip install selenium (Will install the latest version of selenium)
To install specific version of selenium --> pip install selenium==version

pip list --> Gives the list of installed packages along with the version

'''
import time
from selenium import webdriver      ## webdriver is reponsible for the interaction with the browsers

option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)      ## Will prevent the browser from automatically closing

driver = webdriver.Chrome(options=option)
## driver allows us to create driver objects, driver objects will be responsible to work on any browsers


## launch the webpage
## get() --> To launch the webpage. URL should be in the string format
driver.get('https://www.google.com/')
time.sleep(3)

## maximize window
driver.maximize_window()
time.sleep(3)

## minimize
# driver.minimize_window()

## To give full_screen
# driver.fullscreen_window()

## To go back
driver.back()
time.sleep(3)

## forward()
driver.forward()
time.sleep(3)


## To refresh the browser
driver.refresh()

## current_url --> Gives the URL we're launching
print(driver.current_url)   ## current_url is a property        ## https://www.google.com/
# driver.current_url = 'hai'      ## AttributeError: property 'current_url' of 'WebDriver' object has no setter

print(driver.name)      ## chrome
print(driver.title)     ## Google


driver.close()

#-----------------------------------------------------------




























