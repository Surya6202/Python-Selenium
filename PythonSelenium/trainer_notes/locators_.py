'''
web elements : Anything that is present on the webpage is a webelement, It can be textbox, button, link etc,..
represents a HTML element

webelement method :
find_element : To locate any element on the webpage
Syntax : driver.find_element(locator_name, locator_value)

locators : 8 locators
1. id
2. name
3. class name
4. tag name
5. link text
6. partial link text
7. css selector
8. xpath

'''
import time

#-----------------------------------------------------------
# ## id
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=opts)
#
# driver.get('https://www.saucedemo.com/')
# driver.maximize_window()
# time.sleep(3)
#
# ## driver.find_element('locator_name', 'locator_value')
#
# driver.find_element('id', 'user-name').send_keys('standard_user')
# time.sleep(1)
# driver.find_element('id', 'password').send_keys('secret_sauce')
# time.sleep(1)
# driver.find_element('id', 'login-button').click()
#
#
# #---------------------------------------------------------------------
# ## name
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=opts)
#
# driver.get('https://www.saucedemo.com/')
# driver.maximize_window()
# time.sleep(3)
#
# driver.find_element('name', 'user-name').send_keys('standard_user')
# time.sleep(1)
# driver.find_element('name', 'password').send_keys('secret_sauce')
# time.sleep(1)
# driver.find_element('name', 'login-button').click()

#-------------------------------------------------------------------------
## class name
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=opts)
#
# driver.get('https://demowebshop.tricentis.com/')
# driver.maximize_window()
# time.sleep(3)
#
# driver.find_element('class name', 'ico-register').click()
# time.sleep(2)
# driver.find_element('class name', 'ico-login').click()
# time.sleep(2)
# driver.find_element('class name', 'ico-cart').click()

# ## Eg2
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=opts)
#
# driver.get('https://www.saucedemo.com/')
# driver.maximize_window()
# time.sleep(2)
#
# # driver.find_element('class name', 'input_error form_input').send_keys('standard_user')      ## NoSuchElementException
# ## whenever we are using classname locator, the locator value should not have spaces in it.
# ## Incase, we have any spaces, we replace the space with dot(.)
#
# driver.find_element('class name', 'input_error.form_input').send_keys('standard_user')      ## username
# time.sleep(2)
# driver.find_element('class name', 'input_error.form_input').send_keys('secret_sauce')       ## password
#
# ## In the above written example, the username and password will be filled in the same username field.
# ## whenever we have same locator name and locator value for different elements, it will always consider the first match
# ## Indexing is not possible

#--------------------------------------------------------------------------------
# ## tag name
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=opts)
#
# driver.get(r"C:\Users\Ramya\OneDrive\Desktop\selenium\files-20230611T042058Z-001\files\css_selector_dup.html")
# driver.maximize_window()
# time.sleep(3)
#
# driver.find_element('tag name', 'input').send_keys('Sachin')
#
# ## tag name can only locate the first occurance

#-------------------------------------------------------------------
## link text : The text between the anchor tag is a link text,
## The text between any other tag is a normal text

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=opts)
#
# driver.get("https://demowebshop.tricentis.com/")
# driver.maximize_window()
# time.sleep(3)
#
# driver.find_element('link text', 'Register').click()
# time.sleep(2)
# driver.find_element('link text', 'Log in').click()

#-----------------------------------------------------------------------------
## partial link text : same as link text, but we can find the lement by giving the partial portion of that text
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=opts)
#
# driver.get("https://demowebshop.tricentis.com/")
# driver.maximize_window()
# time.sleep(3)
#
# driver.find_element('partial link text', 'Reg').click()
# time.sleep(2)
# driver.find_element('partial link text', 'Log').click()
# time.sleep(2)
# driver.find_element('partial link text', 'Books').click()

#----------------------------------------------------------------------
## css selector --> Whenever we have the attributes which are not locators, we use
## css selector to locate them
## Syntax : tagname[attribute_name="attribute_value"]

## Drawbacks of css selector
## 1. Indexing is not possible (If we are having multiple matches, css selector can only locate the first match)
## 2. Cant locate the texts (Since css selector takes attribute name and attribute value, it cannot locate any text)
## 3. Backtraversing is not possible.
#
# ## Eg1
# from selenium import webdriver
#
# opts =  webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=opts)
#
# driver.get('https://demowebshop.tricentis.com/')
# driver.maximize_window()
# time.sleep(2)
#
# driver.find_element('css selector', 'a[class="ico-register"]').click()
# time.sleep(1.5)
# driver.find_element('css selector', 'input[id="gender-female"]').click()
# time.sleep(1.5)
# driver.find_element('css selector', 'input[id="FirstName"]').send_keys('Virat')
# time.sleep(1.5)
# driver.find_element('css selector', 'input[id="LastName"]').send_keys('Kohli')
# time.sleep(1.5)
# driver.find_element('css selector', 'input[id="Email"]').send_keys('viratkohli@gmail.com')
# time.sleep(1.5)
# driver.find_element('css selector', 'input[id="Password"]').send_keys('virat@1234')
# time.sleep(1.5)
# driver.find_element('css selector', 'input[id="ConfirmPassword"]').send_keys('virat@1234')
#
# # ## Eg2
# # from selenium import webdriver
# #
# # opts =  webdriver.ChromeOptions()
# # opts.add_experimental_option("detach", True)
# #
# # driver = webdriver.Chrome(options=opts)
# #
# # driver.get(r"C:\Users\Ramya\OneDrive\Desktop\selenium\files-20230611T042058Z-001\files\css_selector_dup.html")
# # driver.maximize_window()
# # time.sleep(2)
# #
# # driver.find_element('css selector', 'input[type="text"]').send_keys('Ramya')
# # time.sleep(1)
# # driver.find_element('css selector', 'input[type="text"]').send_keys('Rao')
# #

#----------------------------------------------------------------------------
## xpath
'''
xpath : 2 different types of xpath
1. absolute xpath : Will start from the root. 
                    We use / to indicate absolute xpath 
                    / indicates immediate child
                     
2. relative xpath : Will not start from the root
                    We use // to indicate relative xpath
                    // indicates any child

Syntax :
1. Attribute name and attribute value
        //tagname[@attribute_name="attribute_value"]        ## @ indicates attribute

2. text
        //tagname[text()="text"]

3. Group indexing
        (//tagname[@attribute_name="attribute_value"])[index_number]
        (//tagname[text()="text"])[index_number]

4. using contains
        //tagname[contains(text(), "text")]

'''

# ## absolute xpath
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=opts)
#
# driver.get(r"C:\Users\Ramya\OneDrive\Desktop\selenium\files-20230611T042058Z-001\files\css_selector_dup.html")
# driver.maximize_window()
# time.sleep(2)
#
# driver.find_element('xpath', '(html/body/input)[1]').send_keys('Virat')
# driver.find_element('xpath', '(html/body/input)[2]').send_keys('Kohli')

#-------------------------------------------------------------------
## relative xpath
#
## Attribute name and value
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=opts)
#
# driver.get('https://demowebshop.tricentis.com/')
# driver.maximize_window()
# time.sleep(2)
#
## driver.find_element('xpath', '(html/body/div[4]/div/div/div[2]/div[1]/ul/li/a)[1]').click()     ## absolute xpath for register link
# driver.find_element('xpath', '//a[@class="ico-register"]').click()
# time.sleep(1.5)
# driver.find_element('xpath', '(//input[@name="Gender"])[2]').click()
# time.sleep(1.5)
# driver.find_element('xpath', '//input[@id="FirstName"]').send_keys('Radhika')
# time.sleep(1.5)
# driver.find_element('xpath', '//input[@id="LastName"]').send_keys('Pandit')


#---------------------------------------------
##EG2: Login to saucedemo.com

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=opts)
#
# driver.get('https://www.saucedemo.com/')
# driver.maximize_window()
# time.sleep(2)
#
# driver.find_element('xpath', '//input[@id="user-name"]').send_keys('standard_user')
# time.sleep(1)
# driver.find_element('xpath', '//input[@id="password"]').send_keys('secret_sauce')
# time.sleep(1)
# driver.find_element('xpath', '//input[@id="login-button"]').click()
# time.sleep(2)
#
# driver.find_element('xpath', '//button[@id="react-burger-menu-btn"]').click()
# time.sleep(1)
# driver.find_element('xpath', '//a[@id="logout_sidebar_link"]').click()

#_--------------------------------------------
## text
## Clicking on Register and login of demowebshop using text
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=opts)
#
# driver.get('https://demowebshop.tricentis.com/')
# driver.maximize_window()
# time.sleep(2)
#
# driver.find_element('xpath', '//a[text()="Register"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//a[text()="Log in"]').click()

#----------------------------------------------------
## Login into saucedemo
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=opts)
#
# driver.get('https://www.saucedemo.com/')
# driver.maximize_window()
# time.sleep(2)
#
# driver.find_element('xpath', '//input[@id="user-name"]').send_keys('standard_user')
# time.sleep(1)
# driver.find_element('xpath', '//input[@id="password"]').send_keys('secret_sauce')
# time.sleep(1)
# driver.find_element('xpath', '//input[@id="login-button"]').click()
# time.sleep(2)
#
# driver.find_element('xpath', '//button[text()="Open Menu"]').click()
# time.sleep(1)
# driver.find_element('xpath', '//a[text()="Logout"]').click()

#-----------------------------------------------------------------------
## ASSIGNMENT
## 1. Fill the details in the Signup page of facebook using xpath
## 2. Register by giving all the details in demowebshop using xpath
## 3. Login to swaglabs by using xpath
## 4. Launch Myntra, search for nike, choose bags, select the first bag you see.


#------------------------------------------------------------------------
# ## Group indexing
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=opts)
#
# driver.get(r"C:\Users\Ramya\OneDrive\Desktop\selenium\files-20230611T042058Z-001\files\css_selector_dup.html")
# driver.maximize_window()
# time.sleep(2)
#
# driver.find_element('xpath', '(//input[@type="text"])[1]').send_keys('Rohit')
# time.sleep(1)
# driver.find_element('xpath', '(//input[@type="text"])[2]').send_keys('Sharma')


#-------------------------------------------------------------------------
## Using contains
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=opts)
#
# driver.get('https://demowebshop.tricentis.com/')
# driver.maximize_window()
# time.sleep(2)
#
# driver.find_element('xpath', '(//a[contains(text(), "Books")])[3]').click()
# time.sleep(2)
# driver.find_element('xpath', '(//a[contains(text(), "Computers")])[3]').click()

#---------------------------------------------------------------------------
## ASSIGNMENT

## 1. Login to facebook and then logout
## 2. login to zomato, order the food and cancel.

#---------------------------------------------------------------------
# ## 1. Login to facebook and then logout
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=opts)
#
# driver.get('https://www.facebook.com/')
# driver.maximize_window()
# time.sleep(2)
#
# driver.find_element('xpath', '//input[@id="email"]').send_keys('viratkohli@gmail.com')
# time.sleep(1)
# driver.find_element('xpath', '//input[@placeholder="Password"]').send_keys('virat@1234')
# time.sleep(1)
# driver.find_element('xpath', '//button[text()="Log in"]').click()

#--------------------------------------------------------------------
# ## 2. login to zomato, order the food and cancel.
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=opts)
#
# driver.get('https://www.zomato.com/india')
# driver.maximize_window()
# time.sleep(2)
#
# driver.find_element('xpath', '//h5[text()="Bengaluru Restaurants"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//p[text()="Pizza"]').click()
# time.sleep(2)
# driver.find_element('xpath', '''//h4[text()="Domino's Pizza"]''').click()
# time.sleep(5)

#-----------------------------------------------------------------
## dependent and independent xpath
'''
1. write the xpath of independent element
2. traverse back till we get the common match for both dependent and independent element
3. write the xpath of the dependent element
'''

# ## writing xpath to tick checkbox of ruby in demo.html using group indexing
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=opts)
#
# driver.get(r"C:\Users\Ramya\PycharmProjects\selenium_QCO_SOFPSD_E3\files\demo.html")
# driver.maximize_window()
# time.sleep(2)
#
# driver.find_element('xpath', '(//input[@type="checkbox"])[1]').click()

#----------------------------------------
# ## writing dependent and independent xpath to tick checkbox of ruby in demo.html
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=opts)
#
# driver.get(r"C:\Users\Ramya\PycharmProjects\selenium_QCO_SOFPSD_E3\files\demo.html")
# driver.maximize_window()
# time.sleep(2)
#
# driver.find_element('xpath', '//td[text()="Ruby"]/..//input[@type="checkbox"]').click()

#-------------------------------------------------------------------------
## click on the download link for windows in demo.html
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=opts)
#
# driver.get(r"C:\Users\Ramya\PycharmProjects\selenium_QCO_SOFPSD_E3\files\demo.html")
# driver.maximize_window()
# time.sleep(2)
#
# driver.find_element('xpath', '//td[text()="Windows"]/..//a[text()="Download"]').click()

#-----------------------------------------------------------------
## writing xpath for dynamic values
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=opts)
#
# driver.get(r"C:\Users\Ramya\PycharmProjects\selenium_QCO_SOFPSD_E3\files\demo.html")
# driver.maximize_window()
# time.sleep(2)
#
# element = driver.find_element('xpath', '//td[text()="AAPL"]/..//td[@class="price"]')
# print(element)     ## <selenium.webdriver.remote.webelement.WebElement (session="27321d5928f30dc3f47578a4b3c0e0c1", element="1DD4AC99991CFBB18D5CD4AB36714DEB_element_89")>
# print(element.text)         ## text is a property

#----------------------------------------------------------------
## capture the price of 8gms of gold on Nov 18

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=opts)
#
# driver.get('https://www.moneycontrol.com/news/gold-rates-today/bangalore/')
# driver.maximize_window()
# time.sleep(2)
#
# gold_price = driver.find_element('xpath', '//td[text()="Nov 18, 2023"]/..//td[5]')
# print(gold_price.text)

#--------------------------------------------------------------------------
## 1. Go to python.org, in the downloads, click on the release notes of
##      python 3.8.18 release version
## 2. Capture the text percentage change of SBILife in nseindia.com

#----------------------------------------------------------------------
## 1. Go to python.org, in the downloads, click on the release notes of
##      python 3.8.18 release version

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=opts)
#
# driver.get('https://python.org/')
# driver.maximize_window()
# time.sleep(2)
#
# driver.find_element('xpath', '(//a[text()="Downloads"])[1]').click()
# time.sleep(2)
# driver.find_element('xpath', '//a[text()="Python 3.8.18"]/../..//a[text()="Release Notes"]').click()

#----------------------------------------------------------------------
## 2. Capture the text percentage change of BPCL in nseindia.com
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=opts)
#
# driver.get('https://www.nseindia.com/')
# driver.maximize_window()
# time.sleep(2)
#
# percentage_change = driver.find_element('xpath', '(//a[text()="BPCL"])[1]/../..//td[@class="text-right greenTxt"]')
# print(percentage_change.text)

#_------------------------------------------------------------------

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=opts)
#
# driver.get('https://in.investing.com/currencies/xau-usd')
# driver.maximize_window()
# time.sleep(2)
#
# value = driver.find_element('xpath', '//div[@class="last u-up"]')
# print(value.text)

#------------------------------------------------------------------
'''
1. click on all the checkboxes in demo.html in the given order
    python, ruby, perl, javascript, c#, java   '''

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=opts)
#
# driver.get(r"C:\Users\Ramya\PycharmProjects\selenium_QCO_SOFPSD_E3\files\demo.html")
# driver.maximize_window()
# time.sleep(2)
#
# driver.find_element('xpath', '//td[text()="Python"]/..//input[@type="checkbox"]').click()
# time.sleep(1.5)
# driver.find_element('xpath', '//td[text()="Ruby"]/..//input[@type="checkbox"]').click()
# time.sleep(1.5)
# driver.find_element('xpath', '//td[text()="Perl"]/..//input[@type="checkbox"]').click()
# time.sleep(1.5)
# driver.find_element('xpath', '//td[text()="JavaScript"]/..//input[@type="checkbox"]').click()
# time.sleep(1.5)
# driver.find_element('xpath', '//td[text()="C#"]/..//input[@type="checkbox"]').click()
# time.sleep(1.5)
# driver.find_element('xpath', '//td[text()="Java"]/..//input[@type="checkbox"]').click()
# time.sleep(1.5)


#---------
## Using for loop
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=opts)
#
# driver.get(r"C:\Users\Ramya\PycharmProjects\selenium_QCO_SOFPSD_E3\files\demo.html")
# driver.maximize_window()
# time.sleep(2)
#
# languages = ['Python', 'Ruby', 'Perl', 'JavaScript', 'C#', 'Java']
#
# for language in languages:
#     driver.find_element('xpath', f'//td[text()="{language}"]/..//input[@type="checkbox"]').click()
#     time.sleep(1.5)

#-------------------------------------------------------------------------
'''
find elements 
'''
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=opts)
#
# driver.get(r"C:\Users\Ramya\PycharmProjects\selenium_QCO_SOFPSD_E3\files\demo.html")
# # driver.maximize_window()
# time.sleep(2)
#
# # res = driver.find_element('xpath', '//input[@name="download"]')
# # print(res)          ## webelement of the first match
#
#
# res = driver.find_elements('xpath', '//input[@name="download"]')
# print(res)          ## list of webelements

#---------------------------------------------------------------------
'''To tick all the checkboxes in demo.html using find_elements'''
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=opts)
#
# driver.get(r"C:\Users\Ramya\PycharmProjects\selenium_QCO_SOFPSD_E3\files\demo.html")
# time.sleep(2)
#
# elements = driver.find_elements('xpath', '//input[@name="download"]')
# # print(elements)       ## list of webelements
#
# for web_element in elements:
#     web_element.click()

#---------------------------------------------------------------------------
'''wap to get the text of all the links present in the footer of demowebshop'''
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=opts)
#
# driver.get('https://demowebshop.tricentis.com/')
# time.sleep(2)
#
# footer_link_elements = driver.find_elements('xpath', '//div[@class="footer"]//a')
# print(footer_link_elements)     ## list of webelements
#
# for web_element in footer_link_elements:
#     print(web_element.text)

#------------------------------------------------------------------------
'''wap to get the text of all the links present in the categories of demowebshop'''
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=opts)
#
# driver.get('https://demowebshop.tricentis.com/')
# time.sleep(2)
#
# categories_section = driver.find_elements('xpath', '//div[@class="block block-category-navigation"]//a')
# print(categories_section)       ## list of webelements
#
# for ele in categories_section:
#     print(ele.text)

#-----------------------------------------------------------------------

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=opts)
#
# driver.get('https://www.myntra.com/')
# time.sleep(2)
#
# driver.find_element('xpath', '//input[@class="desktop-searchBar"]').send_keys('Nike')
# time.sleep(2)
# driver.find_element('xpath', '//li[text()="Nike Backpacks"]').click()
# time.sleep(2)
#
# res = driver.find_elements('xpath', '//ul[@class="results-base"]//h4')
# for ele in res:
#     if len(ele.text) !=0:
#         print(ele.text)

#---------------------------------------------------------------
'''
1. wap to print all the link texts present in python.org
2. In Myntra, capture the price of nike shoes along with the shoe name
3. wap to get the discount price on all one plus phones in flipkart
4. In saucedemo.com, wap to print all the product names along with its price
'''



































