
from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("http://demo.actitime.com")

time.sleep(10)
username = driver.find_element_by_xpath("//input[contains(@id, 'username')]")
password = driver.find_element_by_xpath("//input[contains(@name, 'pwd')]")
print("Entering the credentials")
username.send_keys('admin')
password.send_keys('manager')
print('Clearing the text')
username.clear()
password.clear()
print("Entering the credentials again")
username.send_keys('admin1')
password.send_keys('manager1')

time.sleep(5)
driver.close()