from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("https://www.flipkart.com")
driver.implicitly_wait(30)

driver.find_element_by_xpath("//input[contains(@type,'text')]").send_keys('mobiles')
driver.find_element_by_xpath("//button[contains(@type,'submit')]").click()

checkBoxs = driver.find_elements_by_xpath("//span[@class='_1nUZxV']")

for checkBox in checkBoxs:
    checkBox.click()
    time.sleep(1)
    
driver.close()