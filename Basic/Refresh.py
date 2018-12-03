from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("http://demo.actitime.com")

driver.refresh()
time.sleep(5)

driver.close()