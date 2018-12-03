import time
from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.youvisit.com/tour/dartmouth")
driver.implicitly_wait(100)

driver.find_element_by_id("registration-visitortype").click()
driver.find_element_by_xpath("//td[@item-value='prospective_student']").click()
driver.find_element_by_xpath("//td[@item-value='hs_student']//div[contains(text(),'High School Student')]").click()
driver.find_element_by_xpath("//input[@id='firstname']").send_keys('Admin')
driver.find_element_by_xpath("//input[@id='lastname']").send_keys('Manager')
driver.find_element_by_xpath("//input[@id='email']").send_keys("abcd@abc.com")
enrollSelect = driver.find_element_by_id("enrollyear")
selectOption = Select(enrollSelect)
selectOption.select_by_visible_text('2018')

driver.find_element_by_xpath("//input[@name='school_name']").send_keys("ABCD School")
majorProgram = driver.find_element_by_id("major")
selectOption = Select(majorProgram)
selectOption.select_by_visible_text("Ancient History")

gender = driver.find_element_by_id('gender')
selectOption = Select(gender)
selectOption.select_by_visible_text("Male")
driver.find_element_by_xpath("//input[@class='input hasDatepicker']").click()
driver.find_element_by_xpath("(//a[@class='ui-state-default'])[1]").click()
driver.find_element_by_xpath("//input[@id='phone']").send_keys('8105892220')

country = driver.find_element_by_id('country')
selectOption = Select(country)
selectOption.select_by_visible_text('United States')

time.sleep(5)
