
from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("https://demo.vtiger.com/")

time.sleep(10)
credentials = driver.find_element_by_xpath("(//div[@class='marketingDiv widgetHeight']/div)[2]")

print(credentials.text)

time.sleep(5)
driver.close()