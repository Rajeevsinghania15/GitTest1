
from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("http://demo.actitime.com")

time.sleep(10)

loginButton = driver.find_element_by_xpath("(//div[contains(text(), 'Login')])[1]")

print(loginButton.is_enabled())

time.sleep(5)
driver.close()