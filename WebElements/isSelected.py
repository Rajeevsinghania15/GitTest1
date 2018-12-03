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
if loginButton.is_selected():
    print("check box is already selected")
    loginButton.click()
else:
    print("selecting the check box")
    checkBox.click()
    loginButton.click()
    
time.sleep(5)
driver.close()