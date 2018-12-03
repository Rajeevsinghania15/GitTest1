from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("https://www.flipkart.com")
time.sleep(10)

driver.find_element_by_xpath("//input[contains(@type,'text')]").send_keys('Iphone 6')
driver.find_element_by_xpath("//button[contains(@type,'submit')]").click()
time.sleep(3)

driver.find_element_by_xpath("//div[contains(text(),'Apple iPhone 6s (Gold, 32 GB)')]/../../..//input").click()

time.sleep(5)
driver.close()