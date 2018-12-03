from selenium import webdriver


driver = webdriver.Firefox()
driver.get("http://demo.actitime.com")
driver.implicitly_wait(30)

driver.find_element_by_id("username").send_keys('admin')
driver.find_element_by_name("pwd").send_keys('manager')
driver.find_element_by_id("loginButton").click()
driver.find_element_by_id("logoutLink").click()

driver.close()