from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.seleniumhq.org/")
driver.implicitly_wait(30)

download = driver.find_element_by_xpath("//a[@title='Get Selenium']")
download.send_keys(Keys.CONTROL + Keys.ENTER)



handles = driver.window_handles
driver.switch_to_window(handles[1])
time.sleep(5)
driver.find_element_by_xpath("//a[text()='Maven users']").click()

time.sleep(5)
driver.quit()
