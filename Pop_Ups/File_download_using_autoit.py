from selenium import webdriver
import autoit

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://www.seleniumhq.org/")
driver.implicitly_wait(30)

driver.find_element_by_xpath("//a[@title='Get Selenium']").click()
driver.find_element_by_xpath("(//a[@href='https://goo.gl/rW9Yvk'])[1]").click()

autoit.win_active("Opening selenium-server-standalone-3.10.0.jar")
autoit.send("{LEFT}")
autoit.send("{ENTER}")

#driver.close()