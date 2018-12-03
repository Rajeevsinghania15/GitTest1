
from selenium import webdriver
from selenium.webdriver.common.keys  import Keys
import time
driver = webdriver.Chrome()
driver.get("https://demo.vtiger.com/")

time.sleep(10)
username = driver.find_element_by_id("username")

username.send_keys(Keys.CONTROL + 't')
time.sleep(3)
driver.get("http://demo.actitime.com")

time.sleep(5)
driver.close()