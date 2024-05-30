"""
from time import sleep
from selenium.webdriver import ActionChains, Keys
from utilities import chrome_options
from selenium import webdriver

driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(20)
actions = ActionChains(driver)

# There's a scenario like, Open a new tab and then switch back to the last window to complete the other pending
# activities.
# In such scenarios, Selenium helps to handle multiple windows, tabs through window handlers.

# Windows:
# A window in any browser is the main webpage on which the user is landed after hitting a link/URL.
# Such a window in Selenium is referred to as the parent window also known as the main window which opens when
# the Selenium WebDriver session is created and has all the focus of the WebDriver.

# Window Handle:
# It is a unique identifier that holds the address of all the windows.
# It is assumed that each browser will have a unique window handle.
# This window handle function helps to retrieve the handles of all windows.
# A window handle stores the unique address of the browser windows.
# It is just a pointer to a window which returns alphanumeric id in the form of string.
# The window handle in Selenium helps in handling multiple windows and child windows.
# Each browser will have a unique window handle value with which we can uniquely identify it.

# There are two properties in selenium to handle the tabs and windows.
# 1) current_window_handle: This property is used to get the window handle in the form of string by
# this window handle we can perform the required operations and the return type is string.
# 2) window_handles: This property is used to get the window handle of the collection of windows and
# tabs in the form of string by these handles we can perform the required operation and the return type is list[str].
# Then after getting the window handle, we should transfer the driver control to that window or tab and
# we can perform the required operations.

# Transfering the driver control to the window or tab:
# With the help of switch_to property, we can transfer the driver control to the window or tab.
# Upon driver reference, we should call switch_to property and upon this property we should call the window method.
# This method is used to transfer the driver control to the particular window, We've to pass the window handle
# in the form of string.
# The return type of this method is None.

# Handling windows:
# driver.get('https://omayo.blogspot.com/')
# actions.key_down(Keys.SHIFT).click(driver.find_element('id', 'link1')).key_up(Keys.SHIFT).perform()
# window_ids = driver.window_handles
# driver.switch_to.window(window_ids[0])
# print(driver.title, driver.current_url, '', sep='\n')
# driver.switch_to.window(window_ids[1])
# print(driver.title, driver.current_url, sep='\n')

# Handling tabs:
# driver.get('https://www.instagram.com/suryar6202/')
# driver.find_element('xpath', '//div[text() = "Facebook profile + 1 link"]').click()
# driver.find_element('xpath', '//div[text() = "YouTube"]').click()
# window_ids = driver.window_handles
# driver.switch_to.window(window_ids[1])
# shorts = driver.find_element('xpath', '//span[text() = "Anupama famous dialogue"]')
# actions.scroll_to_element(shorts).pause(3).click(shorts).perform()
# like = driver.find_element('xpath', '(//div[@class = "yt-spec-touch-feedback-shape__fill"])[13]')
# actions.pause(3).click(like).pause(3).perform()
# assert driver.find_element('xpath', '//yt-formatted-string[@id = "title" and text() = "Like this video?"]').is_displayed()
# driver.close()
# driver.switch_to.window(window_ids[0])
# actions.click().pause(3).perform()
# print(driver.find_element('tag name', 'h1').text) # I like being an Island Oh My Prabhas 😍

# Creating a new window or tab:
# We can launch multiple applications at a time and we can automate.
# This can with help of method called new_window(), We can create a new window or tab.
# The property switch_to, upon it we should call the new_window method so it'll create a new window or tab and
# transfers the driver control to that new window or tab.
# This method accepts type hint as an argument in the form of string and the type hint would be a 'window' or 'tab'.
# The return type of this method is None.

# driver.get('https://www.netflix.com')
# driver.switch_to.new_window('tab')
# driver.get('https://www.hotstar.com/')
# driver.switch_to.new_window('window')
# driver.get('https://www.zee5.com')
# window_ids = driver.window_handles
# for window_id in window_ids:
#     driver.switch_to.window(window_id)
#     print(driver.current_url, driver.title, sep='\n')
#     print()
# driver.close()
# driver.quit()

# https://www.netflix.com/in/
# Netflix India – Watch TV Shows Online, Watch Movies Online

# https://www.hotstar.com/in/home?ref=%2Fin
# Disney+ Hotstar - Watch TV Shows, Movies, Specials, Live Cricket & Football

# https://www.zee5.com/
# ZEE5 - Watch TV Shows, Web Series, Movies & Live TV Channels

driver.quit()
"""
