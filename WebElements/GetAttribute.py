
from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("http://demo.actitime.com")

time.sleep(10)
username = driver.find_element_by_xpath("//input[contains(@id, 'username')]")
password = driver.find_element_by_xpath("//input[contains(@name, 'pwd')]")

username.send_keys('admin')
password.send_keys('manager')

print("User Name is :",username.get_attribute("value"))
print("Password is :",password.get_attribute("value"))

time.sleep(5)
driver.close()