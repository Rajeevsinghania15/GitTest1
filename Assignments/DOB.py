from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.bankbazaar.com/credit-score.html")
driver.implicitly_wait(30)

driver.find_element_by_xpath("//span[text()='Male']").click()
action = ActionChains(driver)

age = driver.find_element_by_xpath("//div[text()='18']")

action.click_and_hold(age).pause(2)
action.drag_and_drop_by_offset(age, 90, 0)
action.perform()
driver.find_element_by_xpath("//a[contains(text(),'Jun 1987')]").click()
driver.find_element_by_xpath("//a[text()='1']").click()

dob = driver.find_element_by_xpath("//input[@name='dob']")
print(dob.get_attribute("value"))

if dob.get_attribute("value")=="1 Jun 1987":
    print("DOB is correct")
else:
    print("DOB is wrong")

time.sleep(5)
driver.close()
