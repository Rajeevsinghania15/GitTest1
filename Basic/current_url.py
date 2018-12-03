
from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("http://demo.actitime.com")

time.sleep(10)
current_URL = driver.current_url
print('current URL is:',current_URL)
driver.close()