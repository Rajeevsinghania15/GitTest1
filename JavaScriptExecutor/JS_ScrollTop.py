
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("https://demo.vtiger.com/")

driver.execute_script(" window.scrollTo(0, document.body.scrollHeight)")
driver.execute_script(" window.scrollTo(0, document.body.scrollTop)")

time.sleep(2)
driver.close()