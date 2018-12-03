
from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("http://demo.actitime.com")

time.sleep(10)
driver.find_element_by_xpath("//a[text()='Forgot your password?']").click()
time.sleep(5)
driver.close()