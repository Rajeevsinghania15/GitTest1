from selenium import webdriver

from selenium.webdriver.support.wait  import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)

driver.get("https://demo.actitime.com/login.do")
driver.find_element_by_id("username").send_keys('admin')
driver.find_element_by_name("pwd").send_keys('manager')
driver.find_element_by_id("loginButton").click()

wait = WebDriverWait(driver,30)
status = wait.until(EC.title_is('actiTIME - Enter Time-Track'))

print(status, 'page loaded........')
    
driver.close()