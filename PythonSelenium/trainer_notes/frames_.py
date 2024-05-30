import time

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=opts)

driver.get('https://www.globalsqa.com/demo-site/frames-and-windows/#iFrame')
time.sleep(3)

frame_ = driver.find_element('xpath', '//iframe[@name="globalSqa"]')
driver.switch_to.frame(frame_)
time.sleep(2)

driver.find_element('xpath', '//img[@alt="Selenium Online Training"]').click()
time.sleep(2)

#-------------------------------------------------------------------------
import time

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=opts)

driver.get(r'C:\Users\Ramya\PycharmProjects\selenium_QCO_SOFPSD_E3\files\iframe.html')
time.sleep(3)

## switching to frame using id
driver.switch_to.frame('FR1')
time.sleep(2)

driver.find_element('xpath', '//a[text()="Register"]').click()
time.sleep(3)

## switching back to the parent frame
driver.switch_to.parent_frame()
time.sleep(2)

## switching to next frame
driver.switch_to.frame('FR2')
time.sleep(3)

driver.find_element('xpath', '//a[@id="visitsupport"]').click()

#---------------------------------------------------------------------------
## ASSIGNMENT
## 1. Go to https://testpages.eviltester.com/styled/iframes-test.html, in the second frame click on index













