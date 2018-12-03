from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("http://demo/actitime.com")
time.sleep(5)
driver.find_element_by_id("username").send_keys('admin')
driver.find_element_by_name("pwd").send_keys('manager')
driver.find_element_by_id("loginButton").click()
driver.find_element_by_id("logoutLink").click()

driver.close()