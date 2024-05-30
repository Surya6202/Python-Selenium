"""
from time import sleep

from selenium import webdriver
from utilities import chrome_options

driver = webdriver.Chrome(chrome_options)

# Popups:
# It’s a Grapical User Interface window which opens on top of the browser window.
# This popups are used to take some informations from the end-user and give some informations.
# Sometimes these type of popups are used to grab the attention from the end-user
# There are certain types of popups in webpage namely:
# 1) Javascript popup.
# 2) Hidden division popup/ Bootstrap Model popup/ Lightbox popup.
# 3) Notification popup/ Permission popup.
# 4) File upload popup.
# 5) File download popup.
# 6) Authentication popup.

# 1) Javascript popup:
# The popup which is created using JavaScript Language is called as JavaScript popup.
# There are three types of JavaScript Popup.
# Behavior of this popup is:
# * Cannot inspect it.
# * Cannot move/ drag it.
# * It's blockade popup
# 1) Alert Popup.
# 2) Confirmation Popup.
# 3) Prompt Popup.
# All of this can be handled by alert which is a property, upon the driver reference we call switch_to property upon
# this we call alert property.
# This property will return Alert class methods:
# 1) accept(): It's used to accept the alert popup or used to click on the ok button and the return type is none.
# 2) dismiss(): It's used to dismiss the alert popup/ used to click on the cancel button and the return type is none.
# 3) send_keys(): It's is used to send the data to the textfield and the return type is none.
# 4) text: It's used to get the alert text in the popup and the return type is string.

# 1.1) alert_popup:
# In alert popup, we'll have only one option and both the accept() and dismiss() used to handle it.
# These method will work the same as it'll click on the only available option.

# driver.get('https://omayo.blogspot.com/')
# search_button = driver.find_element('id', 'alert1')
# search_button.click()
# alert_popup = driver.switch_to.alert
# print(alert_popup.text)
# alert_popup.accept()
# search_button.click()
# alert_popup.dismiss()

# 1.2) confirmation_popup:
# In this popup, we'll have two options either to accept it or to cancel it.
# It can be handled by accept() and dismiss() methods.

# driver.get('https://omayo.blogspot.com/')
# confirm_button = driver.find_element('id', 'confirm')
# confirm_button.click()
# confirm_popup = driver.switch_to.alert
# print(confirm_popup.text)
# confirm_popup.accept()
# confirm_button.click()
# confirm_popup.dismiss()

# note:
# If try to use send_keys() upon alert or confirmation popup, we'll get 'ElementNotInteractableException'.
# And we'll get a warning as element not interactable: User dialog does not have a text box input field.

# 1.3) prompt_popup:
# In this popup, we'll have to enter the data and click on either ok or cancel button.
# It can be handled by accept(), dismiss() and send_keys() methods.

# driver.get('https://omayo.blogspot.com/')
# prompt_button = driver.find_element('id', 'prompt')
# prompt_button.click()
# prompt_popup = driver.switch_to.alert
# print(prompt_popup.text)
# prompt_popup.send_keys('Surya')
# prompt_popup.accept()
# prompt_button.click()
# prompt_popup.send_keys('Surya')
# prompt_popup.dismiss()

# 2) Hidden division popup:
# It's created by using the html code is called as the hidden division popup.
# Generally 70% of the hidden division popups are created using <div> tag.
# Behavior of this popup is:
# * We can inspect it.
# * We cannot move this popup.
# * Generally, it will be colorful.
# We can handle this popup by inspecting the popup so we can identify it by using findElement() method and handle it
# normally like anyother webelements of the webpage.

# driver.get('https://www.flipkart.com/')
# driver.find_element('xpath', '//span[@role="button"]').click()

# 3) Notification popup:
# It'll occur when we navigate to the url in the browser, it's used to take permission from the end-user for their
# website to show some notifications though the end-user might not be on their Site.
# For Example. Facebook, Amazon etc... notifications will display though they're not on it.
# Behaviors of this Popup:
# * We can’t inspect it.
# * We cannot move it.
# * It generally consists Allow, block and close icon.
# We cannot inspect this popup and there is no library method given in selenium to handle it.
# To handle this popup, We should find a trick to avoid it.
# To avoid this in Chrome, We can disable it by using the ChromeOptions class
# ChromeOptions is a concrete class and we should create the Object of it and call the add_argument() method
# and pass the argument '--disable-notifications', it'll disable the notifications from the webpages.
# To avoid this in other browser, We can disable it by using respective browser options class.

# options = webdriver.ChromeOptions()  # create an instance of chromeoptions class.
# options.add_argument('--start-maximized')  # starts the browser with maximized screen.
# # options.add_argument('--disable-notifications')  # This argument will disable/ block the notifications.
#
# driver = webdriver.Chrome(options)  # pass the options object as an argument and launch the chrome browser.
# driver.get('https://www.justdial.com/')

# 4) File upload popup:
# It'll occur whenever the user needs to upload a file.
# Generally clicking on an upload button in the webpage generates this popup.
# It’s one of the Operating System Level Popups.
# Behaviors of this popup:
# * We can’t inspect it.
# * We can move it.
# * We can maximize and close it.
# We cannot inspect this popup and there is no library method given in selenium to handle it.
# To handle this popup, We should find a trick to avoid it.
# To avoid it, We can use sendKeys() Method to handle it by following below steps:
# 1)  We should check whether there is an input tag within the division of that file upload button
# (Generally 99% of the cases there will an input tag as shown below).
# <input type=”file”> or attributes value should be related to file uploading.
# 2) Use xpath //input[@type=”file” or related locator and identify the element.
# 3) Use sendKeys() and pass the file path to it.

# driver.get('https://omayo.blogspot.com/')
# upload_file = driver.find_element('id', 'uploadfile')
# upload_file.location_once_scrolled_into_view
# upload_file.send_keys(r'D:\Programming\Python\PythonSelenium\basics\assignment.py')

# 5) File download popup:
# It'll occur whenever the user needs to download  some online content.
# It’s also one of the Operating System Level Popups.
# Behaviors of this Popup:
# * We can’t inspect it.
# * We can move it.
# * We can maximize and close it.
# We cannot inspect this popup and there is no library method given in Selenium to handle it.
# To handle this popup, We should find a trick to avoid it.
# To avoid this and download a file:
# 1) We can disable the File Download Popup in respective browsers settings, by turning this option off
# 'Ask where to save each file before downloading'and then run the scripts.
# 2) We can disable it and download the file to the desired location by using the browser Options class.
# In chrome driver, ChromeOptions is a concrete class and we should create the Object of it.
# with object reference call add_experimental_option() method and pass browser preferences as an argument.
# and the argument is (name = 'prefs', value = {'download.default_directory': file_path}).
# By passing this options, all the downloadable files will be downloaded in the specified file directory path.

# file_path = r'D:\Programming\Python\PythonSelenium\downloads' # desired path where files will be downloaded
# options = webdriver.ChromeOptions() # creating 'ChromeOptions instance'.
# options.add_experimental_option('detach', True) # This option will avoid auto termination.
# options.add_argument('--start-maximized') # Launch the chrome browser in maximized mode.
# options.add_experimental_option('prefs', {'download.default_directory': file_path})
# This option will set the file path for files which will be downloaded.

# driver = webdriver.Chrome(options=options)
# driver.get('https://omayo.blogspot.com/p/page7.html')
# driver.find_element('link text', 'ZIP file').click()

# 6) Authentication popup:
# It'll occur whenever we're working with some gateway application and only valid-users are allowed to use this
# application or it'll trigger whenever we're used the sites behind proxy.
# Behaviors of this popup:
# * We can't inspect it.
# * We can't move/ drag it.
# * It's generally has username and password textfields ith ok and cancel button.
# To handle this popup, We should find a trick to avoid it.
# To proceed further by avoiding authentication popup, We should use the username and passwod in the url itself.

# driver.get('https://the-internet.herokuapp.com/basic_auth') # This command will display the popup
# driver.get('https://admin:admin@the-internet.herokuapp.com/basic_auth') # This command will handle the popup
# Here the username is admin and password is admin, We're passing it within the url.

driver.quit()
"""
