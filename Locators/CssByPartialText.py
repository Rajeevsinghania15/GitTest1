from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://demo.actitime.com")
driver.maximize_window()
time.sleep(10)
#Css by prefix string
driver.find_element_by_css_selector("input[name^='u']").send_keys('admin')
#Css by suffix string
driver.find_element_by_css_selector("input[class$='field']").send_keys('manager')
#Css by sub string
driver.find_element_by_css_selector("a[id*='nB']").click()

time.sleep(5)
driver.close()