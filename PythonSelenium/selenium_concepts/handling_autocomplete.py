"""
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from utilities import chrome_options

driver = webdriver.Chrome(chrome_options)

# Autocomplete:
# It's a feature within search box that makes it faster to complete searches that you start to type.
# Our automated systems generate predictions that help people save time by allowing them to quickly complete the
# search they already intended to do.
# These autocomplete is also called as autosuggestions.
# We can handle this autocomplete in selenium by using find_elements methods, by using waiting mechanism and, by using
# ActionChains methods etc...

driver.get('https://www.google.com/')

# by find_elements():
# driver.find_element('id', 'APjFqb').send_keys('Surya')
# auto_sug = driver.find_elements('xpath', '//div[@role = "presentation"]/ul/li')
# for sug in auto_sug:
#     if sug.text.__contains__('actor'):
#         sug.click()
#         break
#     else:
#         pass

# by waiting mechanism:
# 1) Implicit wait:
# driver.implicitly_wait(10)
# driver.find_element('id', 'APjFqb').send_keys('Surya')
# driver.find_element('xpath', '//li[@role = "presentation"]//span[text()="Surya"]').click()

# 2) Explicit wait:
# wait = WebDriverWait(driver, 10)
# driver.find_element('id', 'APjFqb').send_keys('Surya')
# wait.until(expected_conditions.visibility_of_element_located(('xpath', '//div[@role = "presentation"]/ul/li')))
# driver.find_element('xpath', '//li[@role = "presentation"]//span[text()="Surya"]').click()

# by using actions_chains methods:

# actions = ActionChains(driver)
# search_box = driver.find_element('id', 'APjFqb')
# actions.send_keys_to_element(search_box, 'Surya').pause(2).perform()
# suggestions = driver.find_elements('xpath', '//div[@role = "presentation"]/ul/li')
# for i in suggestions:
#     if i.text.__contains__('movies'):
#         actions.click(i).perform()
#         break
#     else:
#         actions.send_keys(Keys.ARROW_DOWN).pause(3).perform()

driver.minimize_window()
driver.quit()
"""