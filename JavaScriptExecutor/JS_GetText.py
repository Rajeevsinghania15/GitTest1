from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https:/demo.actitime.com")

response = driver.execute_script("return document.getElementById('demoCredentials').textContent")
print("Text Of The Element is:",response)

driver.close()