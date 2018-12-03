
from selenium import webdriver
from selenium.webdriver.common.keys  import Keys
import time
driver = webdriver.Firefox()
driver.get("http://demo.actitime.com")

time.sleep(10)
username = driver.find_element_by_id("username")


username.send_keys("Admin")
username.send_keys(Keys.CONTROL + 'a')
time.sleep(3)
username.send_keys(Keys.DELETE)
print(username.get_attribute("value"))


time.sleep(5)
driver.close()