
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("path of the file")
driver.implicitly_wait(30)

doubleClick = driver.find_element_by_xpath("//span[text()='Double Click Here']")
action = ActionChains(driver)
action.double_click(doubleClick).perform()

driver.close()