from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demo.actitime.com/login.do")
driver.implicitly_wait(30)
time.sleep(5)

driver.get_screenshot_as_file("E://Sample.png")
#driver.save_screenshot("E://Sample.png")

driver.close()