
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demo.vtiger.com/index.php")
driver.implicitly_wait(30)

driver.find_element_by_xpath("//button[text()='Sign in']").click()
source = driver.find_element_by_xpath("//b[text()='Sales Pipeline']")
target = driver.find_element_by_xpath("//b[text()='Leads by Status']")

action = ActionChains(driver)
action.drag_and_drop(source, target).perform()

driver.close()