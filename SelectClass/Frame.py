from selenium import webdriver
import time
driver = webdriver.Chrome()

driver.get("https://www.seleniumhq.org/")
driver.maximize_window()
driver.implicitly_wait(30)

driver.find_element_by_xpath("//a[@title='Get Selenium']").click()
driver.find_element_by_link_text("Javadoc").click()
frameEle = driver.find_element_by_xpath("//frame[@src='overview-summary.html']")

#driver.switch_to_frame("classFrame")
#driver.switch_to_frame(2)
driver.switch_to_frame(frameEle)
driver.find_element_by_xpath("(//a[text()='Frames'])[1]").click()


time.sleep(5)
driver.close()