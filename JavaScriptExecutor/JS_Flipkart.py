from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("https://www.flipkart.com/search?q=phones&otracker=start&as-show=on&as=off")
driver.maximize_window()

checkBoxs = driver.find_elements_by_xpath("//span[contains(text(),'Add to Compare')]/../..//input")

for checkBox in checkBoxs:
    driver.execute_script('arguments[0].click()',checkBox)
    time.sleep(2)

driver.close()