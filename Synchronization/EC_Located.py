from selenium import webdriver
from selenium.webdriver.common.by  import By
from selenium.webdriver.support.wait  import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)

driver.get("https://demo.actitime.com/login.do")

wait = WebDriverWait(driver,30)
status = wait.until(EC.element_located_selection_state_to_be((By.ID,'keepLoggedInCheckBox'),False))

if status==True:
    print(status,"Check box is not selected")
else:
    print(status,"Check box is selected")
    
driver.close()