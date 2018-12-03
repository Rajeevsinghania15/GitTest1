
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://github.com/seleniumHQ")
driver.implicitly_wait(30)

action = ActionChains(driver)
seleniumHQ = driver.find_element_by_xpath("//span[text()='www.seleniumhq.org']")
action.click_and_hold(seleniumHQ).release(seleniumHQ).perform()

driver.close()