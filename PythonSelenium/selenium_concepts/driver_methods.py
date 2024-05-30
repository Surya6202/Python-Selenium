"""
from selenium import webdriver
from datetime import datetime

# Selenium requires a web driver, which will help it interface with the browser that you want to run your tests on.
# Webdriver is responsible for the interaction of user agents(browsers).
# The methods in this webdriver fall into three categories:
# 1) Control of the browser itself,
# 2) Selection of WebElements
# 3) Debugging aids.

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
options.add_argument('--start-maximized')

driver = webdriver.Chrome(options=options)
# Creates a new Chrome instance using the default server configuration.
# Webdriver allows us to create driver objects which will be responsible to work on any browsers.
# Based on the certain operations that has to be performed on browser, webdriver has certain browser controlling methods
# and properties:
# get(), title, current_url, page_source, maximize_window(), minimize_window(), fullscreen_window(), forward(), back(),
# refresh(), get_window_size, get_window_position, get_window_rect(), current_window_handle, window_handles, get_screenshot_as_file()
# or save_screenshot(), set_window_size, set_window_position, set_window_rect(), switch_to, name, implicitly_wait(),
# set_page_load_timeout(), execute_script(), close(), quit() etc...

driver.implicitly_wait(10)
# Sets a timeout to implicitly wait for an element to be found, or a command to complete.
# This method only needs to be called one time per session.

driver.set_page_load_timeout(30)
# Set the amount of time to wait for a page load to complete before throwing an error.

driver.maximize_window()
# Maximizes the current window.
# Alternatively for this operation we can use an option, add_argument('--start-maximized')

driver.get('https://www.zee5.com/')
# Loads a web page in the current browser session.
# It's the parameterized method that will accept url in the form of string, and it should be a fully qualified url.
# It has infinite waiting capacity to get loaded the webpage.
# Syntax for url:
# protocol:// host_name// domain_name// port_number// resource_path? query_string# fragment_id
# main url: protocol, host_name and domain_name.
# sub url: port_number, resource_path, query_string, fragment_id.
# Example: "https://www.facebook.com/(main url) 12347698?jdhfgbny2345=tyui/fghdj(sub url)"


driver.fullscreen_window()
# Fullscreen the current window if it is not already fullscreen.
# Alternatively for this operation we can use an option, add_argument('--start-fullscreen')
# To exit fullscreen mode we can do it in three ways
# 1) By using maximize_window()- maximized window
# 2) By using refresh()- default window
# 3) By using Esc key or f11 key

print(driver.current_url)
# Returns the URL of the current page.

print(driver.title)
# Returns the title of the current page.

print(driver.name)
# Returns the name of the browser for this driver instance.

driver.get('https://www.zee5.com/tv-shows/details/shrirasthu-shubhamasthu/0-6-4z5238413')
# To navigate to the subpages we use the same get().

driver.back()
# Navigates to the immediate previous page in the same window.

driver.forward()
# Navigates to the next page, which will be loaded previously.

driver.refresh()
# Reloads the same webpage.

currentWindow = driver.current_window_handle
# Returns the handle of the current window.

print(driver.get_window_size(currentWindow))
# Returns the width and height of the current window in a key-value pair.
# {'width': 1552, 'height': 840}

driver.set_window_size(600, 600, currentWindow)
# Sets the width and height of the current window.

print(driver.get_window_position(currentWindow))
# Returns the x and y position of the current window in a key-value pair.
# {'x': -8, 'y': -8}

driver.set_window_position(10, 10, currentWindow)
# Sets the x and y position of the current window.

print(driver.get_window_rect())
# Returns the x and y coordinates of the window as well as the height and width of the current window in a key-value pair.
# {'height': 840, 'width': 1552, 'x': -8, 'y': -8}

driver.set_window_rect(100, 100, 600, 600)
# Sets the x and y coordinates of the window as well as the height and width of the current window.
# This method is only supported for W3C compatible browsers; other browsers should use set_window_position and set_window_size.

switch = driver.switch_to
# Switches the driver control to the new window/ tab or frames or alert or active webelement.

switch.new_window('window')
# Creates a new window and switches the driver control for further commands of this driver to the new window.

switch.new_window('tab')
driver.get('https://www.zee5.com/tv-shows/details/shrirasthu-shubhamasthu/0-6-4z5238413')
# Creates a new tab and switches the driver control for further commands of this driver
# to the new tab of the same window.

windows = driver.window_handles
# Returns the handles of all windows within the current session.

date_stamp = datetime.now().strftime('%d-%m-%Y')
time_stamp = datetime.now().strftime('%H-%M-%S-%f')
# datetime in PythonProgramming is the combination between dates and times.
# Obtains the current date-time from the system clock in the default time-zone.
# strftime() - used to convert date and time objects to their string representation.

driver.save_screenshot(r'D:/Programming/Python/PythonSelenium/screenshots/'+date_stamp+'_WebpageScreenshot_'+time_stamp+'.png')
# Saves a screenshot of the current window to a PNG image file.
# It's internally performing the operation of get_screenshot_as_file() method.
# We've to pass the file path as an argument in the form of string.

driver.execute_script('window.scrollBy(0, 500)')
# Synchronously executes JavaScript in the current window/frame.

# print(driver.capabilities)
# Returns the drivers current capabilities being used.
# Current browser capabilities:
'''capabilites = {
        'acceptInsecureCerts': False,
        'browserName': 'chrome',
        'browserVersion': '119.0.6045.160',
        'chrome': {
            'chromedriverVersion': '119.0.6045.105 (38c72552c5e15ba9b3117c0967a0fd105072d7c6-refs/branch-heads/6045@{#1103})',
            'userDataDir': 'C:\\Users\\SURYAR~1\\AppData\\Local\\Temp\\scoped_dir6104_824270236'},
        'fedcm:accounts': True,
        'goog:chromeOptions': {'debuggerAddress': 'localhost:61667'},
        'networkConnectionEnabled': False,
        'pageLoadStrategy': 'normal',
        'platformName': 'windows',
        'proxy': {},
        'setWindowRect': True,
        'strictFileInteractability': False,
        'timeouts': {'implicit': 0, 'pageLoad': 300000, 'script': 30000},
        'unhandledPromptBehavior': 'dismiss and notify',
        'webauthn:extension:credBlob': True,
        'webauthn:extension:largeBlob': True,
        'webauthn:extension:minPinLength': True,
        'webauthn:extension:prf': True,
        'webauthn:virtualAuthenticators': True
        }'''

# print(driver.page_source)
# Returns the source of the current page.

driver.minimize_window()
# Minimizes the current window.


driver.close()
# Closes the current window, quitting the browser if it's the last window currently open.
# But the background driver process will not be terminated.

driver.quit()
# Quits this driver, closing every associated window.
# Closes all the windows and tabs associated with that WebDriver session
# Closes the browser process
# Closes the background driver process
# Notify Selenium Grid that the browser is no longer in use so it can be used by another session (if you are using Selenium Grid)
# """