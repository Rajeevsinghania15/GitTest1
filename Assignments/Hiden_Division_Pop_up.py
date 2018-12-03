from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demo.actitime.com/login.do")
driver.implicitly_wait(30)

driver.find_element_by_xpath("//input[@name='username']").send_keys('admin')
driver.find_element_by_xpath("//input[@name='pwd']").send_keys('manager')
driver.find_element_by_xpath("//div[text()='Login ']").click()

driver.find_element_by_xpath("//a[@href='/tasks/tasklist.do']").click()

driver.find_element_by_xpath("//div[contains(text(),'Add New Task')]").click()
driver.find_element_by_xpath("//div[contains(@class,'item createNewTask ellipsis')]").click()
time.sleep(5)

selectCustomer = driver.find_element_by_xpath("//div[contains(@id,'createTasksPopup_customerSelector')]//button")
driver.execute_script("arguments[0].click()",selectCustomer)
bostonCustomer = driver.find_element_by_xpath("//a[contains(text(),'Boston Chocolate')]")
bostonCustomer.click()

selectProjectDD = driver.find_element_by_xpath("//div[contains(@id,'createTasksPopup_projectSelector')]//button")
driver.execute_script("arguments[0].click()",selectProjectDD)
driver.find_element_by_xpath("//a[contains(text(),'Web site creation')]").click()

driver.find_element_by_xpath("(//input[@placeholder='Enter task name'])[1]").send_keys("My_Task")
driver.find_element_by_xpath("(//input[@placeholder='Enter task name'])[1]/../../td[4]").click()
driver.find_element_by_xpath("//a[contains(text(),'design')]").click()
driver.find_element_by_xpath("(//input[@placeholder='Enter task name'])[1]/../../td[5]").click()
driver.find_element_by_xpath("//span[contains(text(),'Create Tasks')]").click()


time.sleep(5)
driver.close()