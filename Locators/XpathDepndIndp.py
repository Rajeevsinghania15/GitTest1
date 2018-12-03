from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("http://www.seleniumhq.org/download/")
time.sleep(5)

driver.find_element_by_xpath("//td[contains(text(),'Python')]/..//a[contains(text(),'Download')]").click()

time.sleep(5)
driver.close()