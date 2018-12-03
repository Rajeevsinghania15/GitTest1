from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("https://www.facebook.com/?stype=lo&jlou=AfchcyAx6dX9bmlzFH5dGYMCSWRwIGvB21QRwOq1UUM3QTdotC0lD6yRRSlLh-2t7VnL8HBkgyNRtx54MREjyW9Qrqob7xIjoPUd-7mGHVdbgw&smuh=31813&lh=Ac8McX-vXYXTjO5K")
driver.maximize_window()
time.sleep(7)

driver.find_element_by_xpath("(//input[contains(@name,'email')])[1]").send_keys('kishorekumar.reddi@gmail.com')
driver.find_element_by_xpath("//input[contains(@id,'pass')]").send_keys('kishore@mca')
driver.find_element_by_xpath("//input[contains(@value,'Log In')]").click()

time.sleep(3)

driver.find_element_by_xpath("//span[contains(text(),'Kishore Kumar')]").click()
time.sleep(2)
driver.find_element_by_xpath("//a[contains(text(),'Home')]").click()
time.sleep(2)

driver.find_element_by_xpath("//div[contains(@id,'userNavigationLabel')]").click()
driver.find_element_by_xpath("//ul[@class='_54nf' and @role='menu']/li[6]").click()


time.sleep(5)
driver.close()