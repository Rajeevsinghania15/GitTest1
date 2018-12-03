
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("http://demo.actitime.com")

driver.maximize_window()

time.sleep(5)

driver.close()