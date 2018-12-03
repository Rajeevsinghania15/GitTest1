
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("https://demo.vtiger.com/")

ele = driver.find_element_by_xpath("//h4[contains(text(),' new in Vtiger Cloud')]")

driver.execute_script("arguments[0].scrollIntoView()",ele)

time.sleep(2)
driver.close()