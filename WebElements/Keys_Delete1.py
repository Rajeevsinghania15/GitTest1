
from selenium import webdriver
from selenium.webdriver.common.keys  import Keys
import time
driver = webdriver.Firefox()
driver.get("https://demo.vtiger.com/")

time.sleep(10)
username = driver.find_element_by_id("username")
password = driver.find_element_by_name("password")


username.send_keys(Keys.CONTROL + 'a')
time.sleep(2)
username.send_keys(Keys.DELETE)
time.sleep(2)
password.send_keys(Keys.CONTROL + 'a')
time.sleep(2)
password.send_keys(Keys.DELETE)


print("User Name is :",username.get_attribute("value"))
print("Password is :",password.get_attribute("value"))

time.sleep(5)
driver.close()