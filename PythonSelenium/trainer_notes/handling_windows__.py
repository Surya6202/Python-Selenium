import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=opts)

driver.get('https://www.ajio.com/')
time.sleep(3)

act_obj = ActionChains(driver)

home_and_living = driver.find_element('xpath', '//a[text()="HOME AND KITCHEN"]')
act_obj.move_to_element(home_and_living).perform()

time.sleep(2)

driver.find_element('xpath', '//a[text()="Wall Decor"]').click()
time.sleep(2)
driver.find_element('xpath', '(//strong[text()="Aawiclo Home"])[1]').click()
time.sleep(3)

handles = driver.window_handles
# print(handles)        #['', '']

driver.switch_to.window(handles[1])
time.sleep(3)
print(driver.title)

driver.find_element('xpath', '//span[text()="ADD TO BAG"]').click()
import time

#---------------------------------------------------------------------------

# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# opts.add_argument("--disable-notifications")
#
# driver = webdriver.Chrome(options=opts)
# act_obj = ActionChains(driver)
#
# ## launch the webpage
# driver.get('https://www.pepperfry.com/')
# time.sleep(10)
#
# ## storing the mouse hovering element
# home_and_decor = driver.find_element('xpath', '//a[@name="Home Decor"]')
# time.sleep(2)
#
# ## hovering to the specified element
# act_obj.move_to_element(home_and_decor).perform()
# time.sleep(2)
#
# ## clicking on some element
# driver.find_element('xpath', '//a[text()="Mandirs "]').click()
# time.sleep(3)
#
# driver.find_element('xpath', '(//img[@alt="Dark Sheesham MDF Floor Rested Mandir With Door"])[1]').click()
# time.sleep(3)
# handles_ = driver.window_handles
#
# ## switching from parent frame to child frame
# driver.switch_to.window(handles_[1])
# time.sleep(3)
# driver.find_element('xpath', '//span[text()="BUY NOW"]').click()


