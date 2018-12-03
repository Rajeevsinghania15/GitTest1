from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.actimind.com/")
driver.implicitly_wait(30)

areaOf = driver.find_element_by_xpath("//a[@href='areas-expertise.html ']")
loc = areaOf.location
xOffset = loc.get('x')
yOffset = loc.get('y')
action = ActionChains(driver)
action.move_by_offset(xOffset, yOffset)
action.perform()

driver.close()