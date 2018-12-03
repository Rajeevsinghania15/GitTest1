
from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("http://demo.actitime.com")

time.sleep(10)
driver.find_element_by_xpath("//input[contains(@id, 'username')]").send_keys('admin')
driver.find_element_by_xpath("//input[contains(@name, 'pwd')]").send_keys('manager')
driver.find_element_by_xpath("(//div[contains(text(), 'Login')])[1]").click()
time.sleep(5)
driver.close()