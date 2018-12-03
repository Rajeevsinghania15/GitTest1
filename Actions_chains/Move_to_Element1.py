from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.istqb.in/")
driver.implicitly_wait(30)

foundation = driver.find_element_by_xpath("//span[text()='FOUNDATION']")
enrollment = driver.find_element_by_xpath("(//span[text()='ENROLLMENT'])[1]")
corporateEnrol  = driver.find_element_by_xpath("//span[text()='CORPORATE ENROLLMENT']")
onlineEnrol = driver.find_element_by_xpath("//span[text()='ONLINE ENROLLMENT']")

action = ActionChains(driver)
action.move_to_element(foundation).pause(1)
action.move_to_element(enrollment).pause(1)
action.move_to_element(corporateEnrol).pause(1)
action.click(onlineEnrol).pause(1)
action.perform()

driver.close()