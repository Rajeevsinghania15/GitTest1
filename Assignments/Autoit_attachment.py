from selenium import webdriver
import autoit
import time
driver = webdriver.Chrome()
driver.get("https://www.gmail.com")
driver.implicitly_wait(30)
#driver.find_element_by_link_text('Gmail').click()
driver.find_element_by_xpath("//a[contains(text(),'Sign In')]").click()

driver.find_element_by_xpath("//input[@type='email' and @jsname='YPqjbf']").send_keys('kishorekumar.reddi@gmail.com')
driver.find_element_by_xpath("//*[@class='CwaK9']").click()

driver.find_element_by_xpath("//input[@type='password' or @name='password']").send_keys('kishore@mca')
driver.find_element_by_xpath("//*[@class='CwaK9']").click()

driver.find_element_by_xpath("//div[text()='COMPOSE']").click()
driver.find_element_by_xpath("//div[@id=':pj']").click()

autoit.win_active("Open")
autoit.control_set_text("Open","Edit1","E:\\kishore\\1.py")
autoit.control_send("Open","Button1","{ENTER}")

time.sleep(5)
driver.close()
