
from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://demo.actitime.com")

browserName = driver.name
print(browserName)
driver.close()