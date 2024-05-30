"""
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from utilities import chrome_options

driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(30)
driver.get('https://omayo.blogspot.com/2013/05/page-one.html')

# ActionChains:
# It's a concrete class that enables advanced user interactions such as mouse and keyboard events.
# This class provides a way to simulate complex user interactions like double-clicking, right-clicking, holding down
# a key, etc.
# By using the ActionChains class, you can interact with a website in the same way a user would, allowing you to test
# more complex interactions that can’t be accomplished with just simple method calls.
# The ActionChains class provides a fluent interface for building and performing actions, which can be performed on
# specific web elements.
# ActionChains is broadly divided into two categories:
# 1) Mouse actions:
# Mouse actions in Selenium are the actions that can be performed using a mouse, such as clicking, double-clicking,
# right-clicking, dragging and dropping, etc. These actions simulate a user’s interactions with a website through
# the mouse.
# 2) Keyboard Actions:
# Keyboard actions in Selenium are the actions that can be performed using a keyboard, such as pressing keys,
# holding down keys, releasing keys, etc. These actions simulate a user’s interactions with a website through the
# keyboard.

# Implementation of ActionChains class:
# 1) Import the ActionChains class from selenium package.
# 'from selenium.webdriver.common.action_chains import ActionChains'
# 2) Create a webdriver instance, 'driver = webdriver.Chrome()'
# 3) Create an instance for ActionChains class and pass the driver reference, duration in milliseconds as a parameter.
# actions = ActionChains(driver=driver, duration=250, devices=None)
# ActionChains constructor arguments:
# driver: The webdriver instance on which the actions will be performed.
# duration: It's the time in milliseconds given to perform for each actions and by default its value is
# 250 milliseconds.
# devices: It's the list of input devices (mouse, keyboard, etc...) to simulate during the execution and by default
# it would be none.
# Note: The arguments like duration and devices are optional.

actions = ActionChains(driver=driver)

# ActionChains Methods:
# All actions will be executed only when the perform() is called upon it as the actions will be stored as an array.
# By calling this method upon webelements, the elements should be available in DOM if not we'll get
# 'NoSuchElementException'.

# 1) click():
# It's used to perform left-click action of the mouse.
# We've to pass webelement as an argument so that it'll click on that element.
# If the argument is none, it'll click on the current position of the mouse which is used to handle a
# 'hidden-division popup'.
# The return type of this method is ActionChains.

# actions.click(on_element=driver.find_element('id', 'drop1')).perform()
# driver.get('https://www.flipkart.com/')
# actions.pause(seconds=5).click().perform()

# 2) click_and_hold():
# It's also used to perform left-click action of the mouse and holds down the left mouse button.
# We've to pass webelement as an argument so that it'll click and hold on that element.
# If the argument is none, it'll click and hold on the current position of the mouse.
# To release the button, We've to use a method called release().
# The return type of this method is ActionChains.

# button = driver.find_element('id', 'drop1')
# actions.click_and_hold(on_element=button).release(on_element=button).perform()
# driver.get('https://www.flipkart.com/')
# actions.pause(seconds=5).click_and_hold().release().perform()

# 3) context_click():
# It's used to perform right click action of the mouse.
# We've to pass webelement as an argument so that it'll click on that element.
# If the argument is none, it'll click on the current position of the mouse.
# The return type of this method is ActionChains.

# actions.context_click(on_element=driver.find_element('id', 'drop1')).perform()
# actions.context_click().perform()

# 4) double_click():
# This method is used to perform left double click action of the mouse.
# We've to pass webelement as an argument so that it'll click on that element.
# If the argument is none, it'll click on the current position of the mouse which is used to handle a
# 'hidden-division popup'.
# The return type of this method is ActionChains.

# actions.double_click(on_element=driver.find_element('id', 'testdoubleclick')).perform()
# driver.get('https://www.flipkart.com/')
# actions.pause(seconds=5).double_click().perform()

# 5) drag_and_drop():
# It's used to perform drag and drop actions of the mouse.
# We've to pass the source and target element as arguments to this method.
# It holds down the left mouse button on the source element, then moves to the target element and releases
# the mouse button.
# The return type of this method is ActionChains.

# driver.get('http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html')
# src_ele = driver.find_element('id', 'box1')
# target_ele = driver.find_element('id', f'box101')
# actions.drag_and_drop(source=src_ele, target=target_ele).perform()

# Alternatively we can use click_and_hold(), release() and move_to_element() or to perform drag_and_drop() operation.
# actions.click_and_hold(on_element=src_ele).move_to_element(to_element=target_ele).release(on_element=target_ele).perform()
# (actions.click_and_hold(on_element=src_ele).move_to_element_with_offset(to_element=target_ele, xoffset=200, yoffset=100)
#  .release(on_element=target_ele).perform())

# 6) drag_and_drop_by_offset():
# It's also used to perform drag and drop action of the mouse but here the target is dependent on co-ordinates.
# We've to pass the source and target element as arguments to this method.
# It holds down the left mouse button on the source element, then moves to the target offset and releases the
# mouse button.
# The return type of this method is ActionChains.

# driver.get('https://jqueryui.com/resources/demos/droppable/default.html')
# src_ele = driver.find_element('id', 'draggable')
# actions.drag_and_drop_by_offset(source=src_ele, xoffset=500, yoffset=400)

# Alternatively we can use click_and_hold(), release() and move_by_offset() to perform drag_and_drop_by_offset() operation.
# actions.click_and_hold(on_element=src_ele).move_by_offset(xoffset=500, yoffset=400).release(on_element=src_ele).perform()

# Note:
# If the methods drag_and_drop and drag_and_drop_by_offset() are not working go with alternative ActionChains methods.

# 7) key_down():
# It is used to perform key press event of the modifier keys.
# It sends a key press only, without releasing it and it should only be used with modifier keys like
# (Control, Alt and Shift).
# With the help of Keys class we can pass the modifier keys as an argument.
# We can also perform the key press event of the modifier key into the webelement, We should pass the webelement as an
# argument along with modifier key.
# The return type of this method is ActionChains.

# actions.key_down(value=Keys.CONTROL).send_keys('A').send_keys('C').perform()
# element = driver.find_element('id', 'ta1')
# element.send_keys('Surya')
# actions.key_down(value=Keys.CONTROL, element=element).send_keys('A').key_down(value=Keys.BACK_SPACE).perform()

# 8) key_up():
# It is used to perform key release event of the modifier keys, After using key_down() we must use this method.
# It releases the modifier keys like (Control, Alt and Shift).
# With the help of Keys class we can pass the modifier keys as an argument.
# We can also perform the key release event of the modifier key into the webelement, We should pass the webelement as an
# argument along with modifier key.
# The return type of this method is ActionChains.

# actions.key_down(value=Keys.CONTROL).send_keys('A').send_keys('C').key_up(value=Keys.CONTROL).perform()
# element = driver.find_element('id', 'ta1')
# element.send_keys('Radhika')
# (actions.key_down(value=Keys.CONTROL, element=element).send_keys('A').
#  key_up(value=Keys.CONTROL).key_down(value=Keys.BACK_SPACE).key_up(value=Keys.BACK_SPACE).perform())

# 9) move_to_element():
# This method is used to perform mouse hovering action.
# It moves the mouse to the middle of an element.
# We've to pass webelement as an argument.
# The return type of this method is ActionChains.

# blogs = driver.find_element('id', 'blogsmenu')
# options = driver.find_elements('xpath', '//li/ul//a')
# actions.move_to_element(to_element=blogs).click(options[2]).perform()

# 10) move_to_element_with_offset():
# This method is used to perform the mouse hovering action.
# It moves the mouse by an offset of the specified element.
# Offsets are relative to the center point of view of the element.
# We've to pass webelement and offsets as arguments.
# If the provided offset value is beyond the view area then we'll get the exception called
# 'MoveTargetOutOfBoundsException'.
# The return type of this method is ActionChains.

# driver.get('http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html')
# src_ele = driver.find_element('id', 'box1')
# target_ele = driver.find_element('id', f'box101')
# (actions.click_and_hold(on_element=src_ele).move_to_element_with_offset(to_element=target_ele, xoffset=100, yoffset=50)
#  .release(on_element=target_ele).perform())

# 11) move_by_offset():
# This method is used to perform the mouse hovering action.
# It moves the mouse to an offset from current mouse position.
# We've to pass offsets as arguments.
# If the provided offset value is beyond the view area then we'll get the exception called
# 'MoveTargetOutOfBoundsException'.
# The return type of this method is ActionChains.

# driver.get('https://jqueryui.com/resources/demos/droppable/default.html')
# src_ele = driver.find_element('id', 'draggable')
# actions.click_and_hold(on_element=src_ele).move_by_offset(xoffset=500, yoffset=40).release(on_element=src_ele).perform()

# 12) pause():
# This method is used to wait for the specified time and after the chained actions will get executed.
# It pauses all the inputs for the specified duration in seconds.
# We've to pass seconds as an arguments.
# The return type of this method is ActionChains.

# driver.get('https://www.makemytrip.com/')
# actions.pause(seconds=5).click().perform()

# 13) perform():
# It's used to execute the single or multiple actions.
# It's the most important method without it we cannot perform any actions.
# The return type of this method is None.

# actions.click(driver.find_element('id', 'drop1')).perform()

# 14) release():
# This method is used to the release the held mouse button.
# It's used to release the held webelement.
# We've to pass the webelement as an argument.
# The return type of this method is ActionChains.

# driver.get('https://www.flipkart.com/')
# actions.pause(seconds=5).click_and_hold().release()

# 15) reset_actions():
# This method is used to reset the actions.
# It clears actions that are already stored locally and on the remote end.
# The return type of this method is None.

# actions.pause(seconds=3).click_and_hold(on_element=driver.find_element('id', 'drop1')).reset_actions()

# 16) scroll_by_amount():
# This method is used to scroll for specified co-ordinates.
# It scrolls by provided amounts with the origin in the top left corner of the viewport.
# The return type of this method is ActionChains.

# actions.scroll_by_amount(delta_x=0, delta_y=400).perform()

# 17) scroll_to_element():
# It is used to scroll the viewport to specified element.
# If the element is outside the viewport, it scrolls to the bottom of the element to the bottom of the viewport.
# The return type of this method is ActionChains.

# button = driver.find_element('class name', 'dropbtn')
# actions.scroll_to_element(button).click(button).perform()

# 18) send_keys():
# This method is used to perform the keyboard actions.
# It sends the keys to current focused webpage or to the webelement.
# The return type of this method is ActionChains.

# element = driver.find_element('id', 'ta1')
# element.send_keys('Surya')
# actions.key_down(value=Keys.CONTROL, element=element).send_keys('A').key_up(value=Keys.CONTROL).perform()

# 19) send_keys_to_element():
# This method is used to enter the data into the text field.
# It works similar to send_keys() webelement method.
# The return type of this method is ActionChains.

# element = driver.find_element('id', 'ta1')
# actions.send_keys_to_element(element, 'Surya').perform()

driver.quit()
"""
