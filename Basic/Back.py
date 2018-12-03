
from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("http://demo.actitime.com")

driver.get("http://www.testyantra.com")
time.sleep(5)

driver.back()
Title = driver.title

if('actiTIME' in Title):
    print('PASS: Navigated back')
else:
    print('FAIL: Back navigation is failed')
driver.maximize_window()

driver.close()