from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://demo.actitime.com")
driver.maximize_window()
time.sleep(10)

driver.find_element_by_css_selector("input#username").send_keys('admin')
driver.find_element_by_css_selector("input[name='pwd']").send_keys('manager')
checkBox = driver.find_element_by_id("keepLoggedInCheckBox")

loginButton = driver.find_element_by_css_selector("a#loginButton")

if loginButton.is_displayed():
    print("Login Button is displaying")
    checkBox.click()
    loginButton.click()
else:
    print("Error: Login Button is not displayed")
    
    
time.sleep(5)
driver.close()