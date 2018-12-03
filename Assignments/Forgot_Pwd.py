import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://buildshop.com")
driver.implicitly_wait(30)

driver.find_element_by_xpath("(//a[contains(text(),'Sign In')])[3]").click()
un = driver.find_element_by_xpath("//input[@title='Email or User Name']")
un.send_keys('kishorekumar.reddi@gmail.com')
pw = driver.find_element_by_xpath("//input[@title='Password']").send_keys('Kishore@mca1')
driver.find_element_by_xpath("//a[contains(text(),'Forgot Password?')]").click()

reun = driver.find_element_by_xpath("//input[@title='Please enter your Email']")
reun.send_keys('kishorekumar.reddi@gmail.com')
driver.find_element_by_xpath("//a[text()='Search']").click()
action = ActionChains(driver)
Email= driver.find_element_by_xpath("(//div[@class='hpmenu'])[2]")
action.context_click(Email).send_keys(Keys.CONTROL + Keys.ENTER).perform()
driver.get("https://www.gmail.com")


#driver.find_element_by_link_text('Gmail').click()

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



time.sleep(5)
