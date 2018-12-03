from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https:/demo.actitime.com")

#driver.find_element_by_id("username").send_keys('admin')
#response = driver.execute_script("return document.getElementById('username').value")

response = driver.execute_script("return document.getElementById('username').value='admin'")
print(response)

driver.close()