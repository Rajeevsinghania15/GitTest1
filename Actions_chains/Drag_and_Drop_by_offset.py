
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demo.vtiger.com/index.php")
driver.implicitly_wait(30)

driver.find_element_by_xpath("//button[text()='Sign in']").click()
source = driver.find_element_by_xpath("//b[text()='Sales Pipeline']")


action = ActionChains(driver)
action.drag_and_drop_by_offset(source, 560,750).perform()

driver.close()