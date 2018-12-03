import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://buildshop.com/")
driver.implicitly_wait(30)

driver.find_element_by_xpath("(//a[@class='NsignupButton'])[2]").click()

driver.find_element_by_xpath("//input[@title='User Name']").send_keys('kishorekumar.r')
driver.find_element_by_xpath("//input[@title='Email']").send_keys('kishore.mc8024@gmail.com')
driver.find_element_by_xpath("//input[@title='Password']").send_keys('Kishore@mca1')
dropDown = driver.find_element_by_xpath("//select[@class='dd-list ddlColor']")
listBox = Select(dropDown)
listBox.select_by_value("3")
driver.find_element_by_xpath("//input[@title='Company Name']").send_keys('xyz')
driver.find_element_by_xpath("//input[@title='Phone']").send_keys('xyz')
driver.find_element_by_xpath("//a[@class='signupP']").click()
newWindow = driver.find_element_by_xpath("//td[@class='vMail']")
newWindow.send_keys(Keys.CONTROL + 't')

driver.get("gmail.com")
time.sleep(5)









