from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("https://demo.actitime.com")
time.sleep(10)
driver.maximize_window()
driver.find_element_by_xpath("//input[@name='username' and @class='textField']").send_keys('admin')
driver.find_element_by_xpath("//*[@name='pwd']").send_keys('manager')
driver.find_element_by_xpath("//a[id='loginButtton' or @class='initial']").click()


time.sleep(5)


driver.close()