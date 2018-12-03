from selenium import webdriver
import time

month = input("Enter the Month: ")
date = input("Enter the Date: ")

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.airindia.com/")
driver.implicitly_wait(30)

driver.find_element_by_xpath("//input[@title='Departing']/..").click()
month_date = driver.find_element_by_xpath("//span[contains(text(),'"+month+"')]/../../..//table//a[text()='"+date+"']")
month_date.click()

time.sleep(15)
driver.close()