from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("http://demo.actitime.com")
driver.maximize_window()
time.sleep(10)

driver.find_element_by_css_selector("input[placeholder='Username']").send_keys('admin')
driver.find_element_by_css_selector("input[name='pwd']").send_keys('manager')
driver.find_element_by_css_selector("a[id='loginButton']").click()

time.sleep(5)
driver.close()