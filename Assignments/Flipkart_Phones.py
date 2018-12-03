from selenium import webdriver
import time


driver = webdriver.Firefox()
driver.get("https://www.flipkart.com")
driver.implicitly_wait(30)

driver.find_element_by_xpath("//input[contains(@type,'text')]").send_keys('phones')
driver.find_element_by_xpath("//button[contains(@type,'submit')]").click()

checkBoxs = driver.find_elements_by_xpath("//span[contains(text(),'Add to Compare')]/../..//input")

for checkBox in checkBoxs:
    driver.execute_script('arguments[0].click()',checkBox)
    time.sleep(2)


    
driver.close()