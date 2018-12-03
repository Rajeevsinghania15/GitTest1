
from selenium import webdriver
from selenium.webdriver.common.keys  import Keys
import time
driver = webdriver.Firefox()
driver.get("http://demo.actitime.com")

time.sleep(10)
username = driver.find_element_by_id("username")
password = driver.find_element_by_name("pwd")

username.send_keys("Admin")
username.send_keys(Keys.CONTROL + 'a')
time.sleep(3)
username.send_keys(Keys.CONTROL + 'c')
time.sleep(3)
password.send_keys(Keys.CONTROL + 'v')
time.sleep(3)
print(password.get_attribute('value'))

time.sleep(5)
driver.close()