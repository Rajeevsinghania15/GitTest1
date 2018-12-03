
from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("http://demo.actitime.com")

driver.minimize_window()
driver.maximize_window()

current_Title = driver.title
print(current_Title)
time.sleep(10)

current_URL = driver.current_url
print('current URL is:',current_URL)

driver.close()