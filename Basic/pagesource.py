
from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("http://demo.actitime.com")

time.sleep(10)
pageSource = driver.page_source

print('length of the source code:',len(pageSource))
driver.close()