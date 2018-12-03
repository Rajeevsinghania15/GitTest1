from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.airindia.com/")
driver.implicitly_wait(30)

driver.find_element_by_xpath("//input[@title='Departing']/..").click()
all_the_dates= driver.find_elements_by_xpath("//span[text()='March']/../../..//*[contains(@class,'ui-state-default')]")

for date in all_the_dates:
    print(date.text)
    if date.is_enabled():
        print(" Date is enabled")
    else:
        print("Date is Disabled")
    
driver.close()