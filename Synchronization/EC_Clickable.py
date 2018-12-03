from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait  import WebDriverWait
import selenium.webdriver.support.expected_conditions  as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)

driver.get("https://demo.actitime.com/login.do")


wait = WebDriverWait(driver,30)
element = wait.until(EC.element_to_be_clickable((By.ID,'loginButton')))

element.click()
print(element)
    
driver.close()