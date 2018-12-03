
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("https://demo.vtiger.com/")

ele = driver.find_element_by_xpath("//h4[contains(text(),' new in Vtiger Cloud')]")

Loc = ele.location
xCoordinates = Loc.get('x')
yCoordinates = Loc.get('y')

driver.execute_script("window.scrollBy(arguments[0],arguments[1])",xCoordinates,yCoordinates)

time.sleep(2)
driver.close()