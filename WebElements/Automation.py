
from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("http://demo.automationtesting.in/")
time.sleep(10)

driver.find_element_by_xpath("//button[contains(@id,'btn2')]").click()
time.sleep(3)
#driver.find_element_by_xpath("//input[contains(@placeholder,'E mail')]").send_keys('admin')
#driver.find_element_by_xpath("//input[contains(@placeholder,'Password')]").send_keys('manager')
#driver.find_element_by_xpath("//img[contains(@src,'enter2.png')]").click()

content = driver.find_element_by_xpath("//div[contains(@class,'col-sm-8 col-xs-8 col-md-8')]/h1")
print(content.text)
driver.find_element_by_xpath("(//a[contains(@href,'#')])[1]").click()
driver.find_element_by_xpath("//a[contains(@href,'FileDownload.html')]").click()
time.sleep(5)
driver.close()