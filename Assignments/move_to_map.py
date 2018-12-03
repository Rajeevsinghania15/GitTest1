from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.youvisit.com/tour/dartmouth")
driver.implicitly_wait(30)

driver.find_element_by_xpath("(//div[@aria-label='Close registration'])[1]").click()
driver.find_element_by_xpath("(//div[@alt='Dartmouth Athletics'])[1]").click()
driver.find_element_by_xpath("(//div[@aria-label='Close registration'])[1]").click()
maxmizedMap = driver.find_element_by_xpath("//div[@class='gm-style-pbc']")
action =ActionChains(driver)
time.sleep(2)
action.move_to_element(maxmizedMap ).perform()
plusSymbol= driver.find_element_by_xpath("(//div[@data-radium='true'])[17]")
if plusSymbol.is_displayed():
    print("Pass:map is maximized")
else:
    print("Fail:map is not maximized")
time.sleep(5)
driver.close()