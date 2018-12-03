import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demo.actitime.com")
driver.implicitly_wait(30)

driver.find_element_by_name("username").send_keys("admin")
driver.find_element_by_name("pwd").send_keys("manager")
driver.find_element_by_id("loginButton").click()

driver.find_element_by_xpath("//div[contains(text(),'TASKS')]").click()
driver.find_element_by_xpath("//div[text()='Add New Task']").click()
driver.find_element_by_xpath("//div[text()='Create new tasks']").click()
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

TaskNames = driver.find_elements_by_xpath("//div[@id='taskListBlock']//tbody//div[@class='title ellipsis']")
print(len(TaskNames))

for TaskName in TaskNames:
    driver.execute_script("arguments[0].scrollIntoView()",TaskName)
    print(TaskName.text)
    
driver.close()