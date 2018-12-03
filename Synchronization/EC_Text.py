from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait  import WebDriverWait
import selenium.webdriver.support.expected_conditions  as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)

driver.get("https://demo.actitime.com/login.do")


wait = WebDriverWait(driver,30)
status = wait.until(EC.text_to_be_present_in_element((By.ID,'keepLoggedInLabel'),'Keep me logged in'))

print(status)
    
driver.close()