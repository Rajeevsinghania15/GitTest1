from selenium import webdriver
from selenium.webdriver.common.by import  By
import time
driver = webdriver.Firefox()
driver.get("http://demo.actitime.com")
time.sleep(10)

username = driver.find_element(By.ID,'username')
username.send_keys('admin')

driver.find_element_by_name('pwd').send_keys('manager')

driver.find_element_by_id('loginButton').click()

time.sleep(5)

driver.close()