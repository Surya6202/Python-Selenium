"""
from selenium import webdriver

options = webdriver.ChromeOptions()
# Options is a class, used to manage various options of a specific driver.

options.add_experimental_option('detach', True)
# It is used to add/ append an experimental option which is passed to the Chrome and Edge browser.
# By default, the chromium driver will quit the session automatically.
# The browser class Chrome and Edge extends the chromium driver.
# To prevent the termination, we use an option 'add_experimental_option('detach', True)'
# We've to pass the option object as an argument to the browser driver.

options.add_argument('--start-maximized')
# This argument will launch the respective driver/ browser in maximized mode.

options.add_argument('--start-fullscreen')
# This argument will launch the respective driver/ browser in fullscreen mode.

options.add_argument('--headless')
# This argument will run the test scripts in headless mode, which means the browser window won't be visible.
# Internally the test script will run without any UI

options.add_argument('--incognito')
# This argument will launch the respective driver/ browser in incognito mode.

options.add_argument('--disable-notifications')
# This argument will block the notification popup.

options.add_experimental_option('prefs', {'download.default_directory': 'file_path'})
# This otion is used to set the download path.

options.add_experimental_option("excludeSwitches", ["enable-automation"])
# This options is used to disable the infobar of the browser instance like
'Chrome is being controlled by automated test software'.
"""