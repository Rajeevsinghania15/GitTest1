
from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("http://demo.actitime.com")
driver.get("http://www.testyantra.com")
time.sleep(5)

driver.back()
time.sleep(5)

driver.forward()
time.sleep(5)

print('Clicking on the forward button')
Title = driver.title
print('Title of the page is : ', Title)
if('Test Yantra' in Title):
    print('PASS: Navigated forward')
else:
    print('FAIL: forward navigation is failed')
driver.close()