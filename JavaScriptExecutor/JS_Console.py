from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://demo.actitime.com")

response = driver.execute_script("return console.log('Welcome')")
print("Response from the browser console window:",response)

driver.close()