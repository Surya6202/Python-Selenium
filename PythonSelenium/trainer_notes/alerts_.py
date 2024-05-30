'''
Alerts : Alerts are not inspectable. We have to handle them using javascript

1. simple alert : It will have only one option
2. Confirmation alert : It will have two options. ok/cancel, yes/no,..
3. Authentication popup


'''

## Simple Alert
import time

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=opts)

driver.get('https://demowebshop.tricentis.com/')
time.sleep(2)

driver.find_element('xpath', '//input[@value="Search"]').click()
time.sleep(3)

alert_obj = driver.switch_to.alert
# alert_obj.accept()
alert_obj.dismiss()
#
# ## Incase of simple alerts, both accept() and dismiss() will work the same. It will click on the only available option


#------------------------------------------------------------------------
## confirmation
#
import time

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=opts)

driver.get('https://the-internet.herokuapp.com/')
time.sleep(2)

driver.find_element('xpath', '//a[text()="JavaScript Alerts"]').click()
time.sleep(2)

driver.find_element('xpath', '//button[text()="Click for JS Confirm"]').click()
time.sleep(2)

alert_ = driver.switch_to.alert
alert_.accept()
time.sleep(1)

driver.find_element('xpath', '//button[text()="Click for JS Confirm"]').click()
time.sleep(2)
alert_.dismiss()

#-----------------------------------------------------------------------
## Aunthentication popup

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=opts)

driver.get('https://the-internet.herokuapp.com/basic_auth')
time.sleep(2)

## In the above code, we will get a popup to give username and pwd.
## Since popups are not inspectable,we give the credentials while launching the webpage itself

## https://username:pwd@url

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=opts)

driver.get('https://admin:admin@the-internet.herokuapp.com/basic_auth')
time.sleep(2)

#---------------------------------------------------------------------
## file-upload
#
from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=opts)

driver.get('https://www.foundit.in/')
time.sleep(2)

driver.find_element('xpath', '//div[contains(text(), "Upload Resume")]').click()
time.sleep(2)

path = r'C:\Users\Ramya\PycharmProjects\selenium_QCO_SOFPSD_E3\files\python_resume.doc'
driver.find_element('xpath', '//input[@id="file-upload"]').send_keys(path)

#-------------------------------------------------------------------
## ASSIGNMENT :
## Go to https://testautomationpractice.blogspot.com/ and handle alerts





















