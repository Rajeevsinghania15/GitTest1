from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("checkBox path")
driver.implicitly_wait(30)

checkBoxs = driver.find_elements_by_xpath("//input[@type='checkbox']")

for checkBox in checkBoxs:
    checkBox.click()
    time.sleep(1)
    
driver.close()