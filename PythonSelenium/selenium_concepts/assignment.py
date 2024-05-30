from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utilities import chrome_options

driver = webdriver.Chrome(chrome_options)
driver.implicitly_wait(20)
wait = WebDriverWait(driver, 30)
actions = ActionChains(driver)

# 1)
# driver.get('https://www.facebook.com/signup')
# driver.find_element('xpath', '//input[@name = "firstname"]').send_keys('Surya')
# driver.find_element('xpath', '//input[@name = "lastname"]').send_keys('R')
# driver.find_element('xpath', '//input[@name="reg_email__"]').send_keys('9876543210')
# driver.find_element('xpath', '//input[@name="reg_passwd__"]').send_keys('12345')
# driver.find_element('xpath', '//input[@value="2"]').click()
# driver.find_element('xpath', '//button[@name="websubmit"]').click()

# 2)
# driver.get('https://demowebshop.tricentis.com/')
# driver.find_element('xpath', '//a[text()="Register"]').click()
# driver.find_element('xpath', '//input[@id="gender-male"]').click()
# driver.find_element('xpath', '//input[@id="FirstName"]').send_keys('Surya')
# driver.find_element('xpath', '//input[@id="LastName"]').send_keys('R')
# driver.find_element('xpath', '//input[@id="Email"]').send_keys('surya123@gmail.com')
# driver.find_element('xpath', '//input[@id="Password"]').send_keys('Surya123')
# driver.find_element('xpath', '//input[@id="ConfirmPassword"]').send_keys('Surya123')
# driver.find_element('xpath', '//input[@id="register-button"]').submit()

# 3)
# driver.get('https://www.saucedemo.com/')
# driver.find_element('xpath', '//input[@id = "user-name"]').send_keys('standard_user')
# driver.find_element('xpath', '//input[@id = "password"]').send_keys('secret_sauce')
# driver.find_element('xpath', '//input[@id = "login-button"]').submit()

# 4)
# driver.get('https://www.myntra.com/')
# driver.find_element('xpath', '//input[@class="desktop-searchBar"]').send_keys('nike bags')
# driver.find_element('xpath', '//a[@class="desktop-submit"]').click()
# driver.find_element('xpath', '//h3[text() = "Nike"]').click()

# 5)
# driver.get('https://www.facebook.com/')
# driver.find_element('id', 'email').send_keys('**************')
# driver.find_element('id', 'pass').send_keys('********')
# driver.find_element('name', 'login').submit()
# driver.find_element('xpath', '//div[contains(@aria-label, "Account controls")]//div[contains(@class, "x1rg5ohu x")]').click()
# driver.find_element('xpath', '//span[text()="Log out"]').click()

# 6)
# driver.get('https://www.zomato.com/india')
# resturant = driver.find_element('xpath', '//h5[text()="Bengaluru Restaurants"]')
# resturant.location_once_scrolled_into_view
# resturant.click()
# driver.find_element('xpath', '//p[text() = "Biryani" ]/parent::a').click()
# driver.find_element('xpath', '//h4[text()="Nandhini Deluxe"]/../..').click()

# 7)
# driver.get('https://python.org/')
# driver.find_element('xpath', '(//a[text()="Downloads"])[1]').click()
# driver.find_element('xpath', '//a[text()="PythonProgramming 3.8.18"]/../..//span[@class="release-enhancements"]').click()

# 8)
# driver.get('https://www.nseindia.com/')
# element = driver.find_element('xpath', '//a[text()="BPCL"]/../..//td[contains(@class,"greenTxt")]')
# element.location_once_scrolled_into_view
# print(element.text)

# 9)
# driver.get('https://python.org/')
# count = 0
# elements = driver.find_elements('xpath', '//body//a')
# for link in elements:
#     count += 1
#     print(link.get_attribute('href'))
# print(count)

# 10)
# driver.get('https://www.myntra.com/')
# driver.find_element('xpath', '//input[@class="desktop-searchBar"]').send_keys('nike shoe')
# driver.find_element('xpath', '//a[@class="desktop-submit"]').click()

# individual shoe:
# shoe_name = driver.find_element('xpath', '//h4[contains(text(),"Men Running")]/preceding::h3').text
# shoe_price = driver.find_element('xpath', '//h4[contains(text(),"Men Running")]/..//span[@class="product-discountedPrice"]').text
# print(shoe_price, shoe_name, sep='\n')

# All shoes:
# brands = driver.find_elements('xpath', '//h3[text()="Nike"]')
# shoes = driver.find_elements('xpath', '//h3[text()="Nike"]/following::h4[@class="product-product"]')
# prices = driver.find_elements('xpath', '//h3[text()="Nike"]/..//span[@class="product-discountedPrice"]')
# product_brand, product, product_price, complete_product = [], [], [], []
# for brand in brands:
#     product_brand.append(brand.text)
# for shoe in shoes:
#     product.append(shoe.text)
# for price in prices:
#     product_price.append(price.text)
# for i in range(0, len(product_price)):
#     complete_product.append(product_brand[i]+'_'+product[i])
# details = {}
# for i in range(0, len(product_price)):
#     if complete_product[i] not in details:
#         details[complete_product[i]] = product_price[i]
#     else:
#         details[complete_product[i]+str(i)] = product_price[i]
# print(details)

# 11)
# driver.get('https://www.flipkart.com/')
# driver.find_element('xpath', '//span[@role="button"]').click()
# driver.find_element('name', 'q').send_keys('one plus phone')
# driver.find_element('xpath', '//button[@type="submit"]').submit()
# discounted_prices = driver.find_elements('xpath', '//div[contains(text(),"OnePlus")]/../..//div[@class="_30jeq3 _1_WHN1"]')
# discounted_price = []
# for i in discounted_prices:
#     discounted_price.append(i.text)
# print(discounted_price)

# 12)
# driver.get('https://www.saucedemo.com/')
# driver.find_element('xpath', '//input[@id = "user-name"]').send_keys('standard_user')
# driver.find_element('xpath', '//input[@id = "password"]').send_keys('secret_sauce')
# driver.find_element('xpath', '//input[@id = "login-button"]').submit()
# products = driver.find_elements('xpath', '//a[@href="#"]/div')
# prices = driver.find_elements('xpath', '//a[@href="#"]/div/../../..//div[@class="inventory_item_price"]')
# product, product_price = [], []
# for i in products:
#     product.append(i.text)
# for i in prices:
#     product_price.append(i.text)
# details = {}
# for i in range(0, len(product_price)):
#     if product[i] not in details:
#         details[product[i]] = product_price[i]
#     else:
#         details[product[i] + str(i)] = product_price[i]
# print(details)

# 13)
# driver.get('https://testautomationpractice.blogspot.com/')
# countries = driver.find_element('id', 'country')
# countries.location_once_scrolled_into_view
# select = Select(countries)
# select.select_by_visible_text('India')

# 14)
# driver.get('https://www.shaadi.com/')
# driver.execute_script('window.scrollBy(0, 300)')
# driver.find_element('xpath', '//div[contains(@data-testid, "gender")]/child::div').click()
# driver.find_element('xpath', '//div[contains(@data-testid, "gender")]//following::div[text()="Man"]').click()
# driver.find_element('xpath', '//div[contains(@data-testid,"age_from")]').click()
# driver.find_element('xpath', '//div[contains(@data-testid,"age_from")]/descendant::div[text() = "26"]').click()
# driver.find_element('xpath', '//div[contains(@data-testid,"age_to")]').click()
# driver.find_element('xpath', '//div[contains(@data-testid,"age_to")]/descendant::div[text() = "31"]').click()
# driver.find_element('xpath', '//label[text() = "of religion"]/../descendant::div[text() = "Select"]').click()
# driver.find_element('xpath', '//div[text() = "Select"]/following::div[text() = "Hindu"]').click()
# driver.find_element('xpath', '//label[contains(text(), "mother")]/..//div[text() = "Select"]').click()
# driver.find_element('xpath', '//div[text() = "Select"]/following::div[text() = "Frequently Used"]/following-sibling::div[text() = "Telugu"]').click()
# driver.find_element('xpath', '//div[contains(@data-testid,"age_from")]').click()
# driver.find_element('xpath', '//div[contains(@data-testid,"age_from")]/descendant::div[text() = "26"]').click()
# driver.find_element('xpath', '//button[text() = "Let\'s Begin"]').click()

# 15)
# driver.get('https://www.naukri.com/')
# driver.find_element('xpath', '//input[contains(@placeholder ,"Enter skills")]').send_keys('Automation Testing')
# driver.find_element('id', 'expereinceDD').click()
# driver.find_element('xpath','//div/following::li//span[text() = "Fresher"]').click()
# driver.find_element('xpath', '//input[@placeholder = "Enter location"]').send_keys('Hosur')
# driver.find_element('xpath', '//div[text() = "Search"]').click()

# 16)
# driver.get('https://www.airbnb.co.in/')
# actions.pause(5).click().perform()
# locations = wait.until(expected_conditions.visibility_of_all_elements_located(
#     ('xpath', '//div/following::div[@data-testid="listing-card-title"]')))
# rates = wait.until(
#     expected_conditions.visibility_of_all_elements_located(('xpath', '//div/descendant::span[@class="_tyxjp1"]')))
# places, prices = [], []
# for i in locations:
#     places.append(i.text)
# for j in rates:
#     prices.append(j.text)
# farms_detail = {}
# for i in range(0, len(places)):
#     farms_detail[places[i]] = prices[i]
# print(farms_detail)

# 17)
# driver.get('https://www.shaadi.com/')
# driver.execute_script('window.scrollBy(0, 300)')
# religions, languages, other_languages = [], [], []
# driver.find_element('xpath', '//label[text() = "of religion"]/../descendant::div[text() = "Select"]').click()
# religion = driver.find_elements('xpath', '//div[@class="Dropdown-option"]')
# for i in religion:
#     religions.append(i.text)
# driver.find_element('xpath', '//label[contains(text(), "mother")]/..//div[text() = "Select"]').click()
# language = driver.find_elements('xpath', '//div[text() = "Frequently Used"]/following-sibling::div')
# other_language = driver.find_elements('xpath', '//div[text() = "More"]/following-sibling::div')
# for i in language:
#     languages.append(i.text)
# for i in other_language:
#     other_languages.append(i.text)
#
# print(f'The religions are {religions}', f'The indian languages are {languages}', f'The other languages are {other_languages}', end='' ,sep='\n')

# 18)
# driver.get('https://www.foundit.in/')
# actions = ActionChains(driver)
# actions.pause(3).move_to_element(driver.find_element('xpath', '//a[contains(text(), "Skill Tests")]')).pause(3).perform()
# driver.find_element('xpath', '//ul/h4[contains(text(), "Back-end Developer")]/..//a[contains(text(), "Python")]').click()

# 19)
# driver.get('https://www.ajio.com/')
# actions = ActionChains(driver)
# actions.move_to_element((driver.find_element('link text', 'HOME AND KITCHEN'))).perform()
# driver.find_element('link text', 'Wall Decor').click()

# 20)
# driver.get('http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html')
# actions = ActionChains(driver)
# for i in range(1, 8):
    # src_ele = driver.find_element('id', f'box{i}')
    # target_ele = driver.find_element('id', f'box10{i}')
    # actions.drag_and_drop(src_ele, target_ele).perform()

# 21)
# driver.get('https://testautomationpractice.blogspot.com/')

# 22)
# driver.get('https://www.makemytrip.com/')
# actions.pause(5).click().perform()
# driver.find_element('xpath', '//span[text() = "Departure"]').click()
# month = driver.find_element('xpath', '(//div[@class = "DayPicker-Caption"]/div)[1]').text
# while not month.__eq__('February 2025'):
#     driver.find_element('xpath', '//div[@class = "DayPicker-NavBar"]/child::span[contains(@class, "next")]').click()
#     month = driver.find_element('xpath', '(//div[@class = "DayPicker-Caption"]/div)[1]').text
# driver.find_element('xpath', '//p[text()="6"]/..').click()
# assert wait.until(expected_conditions.visibility_of_element_located(('xpath', '//span[text() = "6"]'))).is_displayed()

# 23)
# driver.get('https://in.hotels.com/')
# calendar = driver.find_element('name', 'EGDSDateRange-date-selector-trigger')
# calendar.click()
# month = driver.find_element('xpath', '(//span[@class = "uitk-align-center uitk-month-label"])[1]').text
# while not month.__eq__('February 2025'):
#     driver.find_element('xpath', '//button[@data-stid="uitk-calendar-navigation-controls-next-button"]').click()
#     month = driver.find_element('xpath', '(//span[@class = "uitk-align-center uitk-month-label"])[1]').text
# driver.find_element('xpath', '(//div[text() = "6"])[1]').click()
# driver.find_element('xpath', '//button[@data-stid="apply-date-selector"]').click()
# assert '6 Feb' in calendar.text

# 24)
# driver.get('https://www.irctc.co.in/')
# driver.find_element('xpath', '//span[contains(@class, "ui-calendar")]/input').click()
# month = driver.find_element('xpath', '//span[contains(@class,"ui-datepicker-month")]').text
# year = driver.find_element('xpath', '//span[contains(@class,"ui-datepicker-year")]').text
# while not (month.__eq__('September') and year.__eq__('2024')):
#     driver.find_element('xpath', '//span[contains(@class,"ui-datepicker-next-icon")]').click()
#     month = driver.find_element('xpath', '//span[contains(@class,"ui-datepicker-month")]').text
#     year = driver.find_element('xpath', '//span[contains(@class,"ui-datepicker-year")]').text
# driver.find_element('link text', '6').click()
# driver.screenshot('Date1.jpg')

# 25)
# driver.get('https://www.facebook.com/')
# element = driver.find_element('name', 'login')
# colors = ['aqua', 'blue', 'fuchsia', 'gray', 'green', 'lime', 'maroon', 'gold', 'silver', 'pink', 'red']
# for color in colors:
#     driver.execute_script(f'arguments[0].style.background="{color}"', element)
#     sleep(2)

# driver.get('https://pagalworld.cool/kavalaya-jailer-mp3-song-download.html')
# driver.find_element('xpath','//a[text()="Download 320 kbps - 7.53 mb"]').click()

sleep(5)
driver.quit()

















# marks = [50,66,23]
# print(f"Smallest number is {min(marks)}")


# N = 3
# for i in range(0,N,1):
#     for j in range (N,0,-1):
#         for k in range(N,i,-1):
#             print(j, end='')
#     print()


# # m1=int(input('Enter marks for s1: \n'))
# # m2=int(input('Enter marks for s2: \n'))
# # m3=int(input('Enter marks for s3: \n'))
#
# m1,m2,m3 = map(int,input('Enter the marks:\n').split(" "))
# if (m1 or m2 or m3)<=0 or (m1 or m2 or m3)>100:
#     quit()
# cal=lambda s1,s2,s3:min(s1,s2,s3)
# print(f"Smallest number is {cal(m1,m2,m3)}")

















