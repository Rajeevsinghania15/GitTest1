from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.actimind.com/")
driver.implicitly_wait(30)

action = ActionChains(driver)
aboutCompany = driver.find_element_by_xpath("(//a[contains(@href,'about-company.html')])[1]")
action.context_click(aboutCompany).perform()

time.sleep(5)
driver.close()