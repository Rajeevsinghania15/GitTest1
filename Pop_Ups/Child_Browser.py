from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.seleniumhq.org/")
driver.implicitly_wait(30)

download = driver.find_element_by_xpath("//a[@title='Get Selenium']")

download.send_keys(Keys.CONTROL + Keys.ENTER)
all_wndow_handles = driver.window_handles

for handle in all_wndow_handles:
    print(handle)
time.sleep(5)
driver.quit()
