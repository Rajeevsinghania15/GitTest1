import time
from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.youvisit.com/tour/dartmouth")
driver.implicitly_wait(30)

driver.find_element_by_xpath("//div[@title='I am a *']").click()
driver.find_element_by_xpath("(//div[text()='Student'])[1]").click()
driver.find_element_by_xpath("//div[contains(text(),'High School Student')]").click()

driver.find_element_by_xpath("//input[@id='firstname']").send_keys('kishore')
driver.find_element_by_xpath("//input[@id='lastname']").send_keys('kumar')

driver.find_element_by_xpath("//input[@id='email']").send_keys('kishorekumar.reddi@gmail.com')

dropDown = driver.find_element_by_xpath("//select[@id='enrollyear']") 
ListBox = Select(dropDown)
ListBox.select_by_value("2018")

driver.find_element_by_xpath("//input[@name='school_name']").click()

responce = driver.find_element_by_xpath("//input[@name='school_name']")
responce.send_keys('school')

driver.find_element_by_xpath("//ul[@id='ui-id-1']/li[3]").click()

drop = driver.find_element_by_xpath("//select[@id='major']")
List = Select(drop)
List.select_by_visible_text("Biological Sciences")

gender = driver.find_element_by_xpath("//select[@id='gender']")
Option =  Select(gender)
Option.select_by_value("Male")

driver.find_element_by_xpath("//input[@id='phone']").send_keys('9989596202')

country = driver.find_element_by_xpath("//select[@id='country']")
Choose = Select(country)
Choose.select_by_value("IND")

driver.find_element_by_xpath("//input[@id='intl_street']").send_keys('Bobbili')
driver.find_element_by_xpath("//input[@id='intl_city']").send_keys('Vizianagaram')

driver.find_element_by_xpath("//input[@id='intl_state']").send_keys('AndhraPradesh')
driver.find_element_by_xpath("//input[@id='intl_postal']").send_keys('535558')

time.sleep(5)
driver.close()