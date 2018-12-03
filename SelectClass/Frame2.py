from selenium import webdriver
import time
driver = webdriver.Chrome()

driver.get("https://www.seleniumhq.org/")
driver.maximize_window()
driver.implicitly_wait(30)

driver.find_element_by_xpath("//a[@title='Get Selenium']").click()
driver.find_element_by_link_text("Javadoc").click()
frameEle = driver.find_element_by_xpath("//frame[@src='overview-summary.html']")

driver.switch_to.frame(frameEle)
texts= driver.find_element_by_xpath("//div[@class='contentContainer']").text
print(texts)

driver.switch_to.default_content()
driver.switch_to.frame("packageListFrame")

driver.find_element_by_xpath("//a[@href='com/thoughtworks/selenium/package-frame.html']").click()

time.sleep(5)
driver.close()