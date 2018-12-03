from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.actimind.com/")
driver.implicitly_wait(30)

areaOf = driver.find_element_by_xpath("//a[@href='areas-expertise.html ']")
office = driver.find_element_by_xpath("//a[contains(text(),'MS Office Plug-ins')]")
action = ActionChains(driver)
action.move_to_element(areaOf).click(office).perform()


driver.close()