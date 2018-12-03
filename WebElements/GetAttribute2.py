 
from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("https://demo.vtiger.com/")

time.sleep(10)
username = driver.find_element_by_id("username")
password = driver.find_element_by_name("password")

print("User Name is :",username.get_attribute("value"))
print("Password is :",password.get_attribute("value"))

time.sleep(5)
driver.close()