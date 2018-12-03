from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://demo.actitime.com")
A = 5
response = driver.execute_script("return console.log('value of A is: arguments[0]')",A)
print("Response from the browser console window after printing a value:",response)

driver.close()