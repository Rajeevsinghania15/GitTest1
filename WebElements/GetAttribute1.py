
from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("http://demo.actitime.com")

time.sleep(10)
username = driver.find_element_by_xpath("//input[contains(@id, 'username')]")
password = driver.find_element_by_xpath("//input[contains(@name, 'pwd')]")

username.send_keys('admin')
password.send_keys('manager')

print("Proparty Name is :",username.get_attribute("name"))


time.sleep(5)
driver.close()