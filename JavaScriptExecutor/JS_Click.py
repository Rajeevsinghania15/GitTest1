from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("https:/demo.actitime.com")

response = driver.execute_script("return document.getElementById('loginButton').click()")
print(response)
time.sleep(2)
driver.close()