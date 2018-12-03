
from selenium import webdriver
from selenium.webdriver.common.keys  import Keys
import time
driver = webdriver.Firefox()
driver.get("http://demo.actitime.com")

time.sleep(10)
username = driver.find_element_by_id("username")


username.send_keys("AdminManagerAdmin")

count = len(username.get_attribute("value"))

for i in range(count+1):
    username.send_keys(Keys.BACK_SPACE)
    time.sleep(1)

driver.close()