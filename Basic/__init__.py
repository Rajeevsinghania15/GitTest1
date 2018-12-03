from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("http://demo.actitime.com")
time.sleep(10)
driver.close()