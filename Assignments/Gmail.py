from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("https://www.gmail.com")
driver.maximize_window()
time.sleep(5)
#driver.find_element_by_link_text('Gmail').click()

time.sleep(3)
driver.find_element_by_xpath("//input[@type='email' and @jsname='YPqjbf']").send_keys('kishorekumar.reddi@gmail.com')
driver.find_element_by_xpath("//*[@class='CwaK9']").click()

time.sleep(2)
driver.find_element_by_xpath("//input[@type='password' or @name='password']").send_keys('kishore@mca')
driver.find_element_by_xpath("//*[@class='CwaK9']").click()

time.sleep(3)
driver.find_element_by_xpath("//a[contains(@title,'Inbox')]").click()
driver.find_element_by_xpath("//span[contains(@id,':3e')]").click()
time.sleep(1)
driver.find_element_by_xpath("//div[contains(@class,'ar6 T-I-J3 J-J5-Ji')]").click()

time.sleep(2)
driver.find_element_by_xpath("(//a[contains(@target,'_top')])[11]").click()
time.sleep(3)

driver.find_element_by_xpath("//span[contains(@class,'gb_ab gbii')]").click()
driver.find_element_by_xpath("//a[contains(text(),'Sign out')]").click()

time.sleep(5)
driver.close()
