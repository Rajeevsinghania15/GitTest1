from selenium import webdriver

import time
driver = webdriver.Firefox()
driver.get("http://demo.actitime.com")
time.sleep(10)

Credentials = driver.find_element_by_id("demoTooltipContainer")
print(Credentials.text)

time.sleep(5)

driver.close()