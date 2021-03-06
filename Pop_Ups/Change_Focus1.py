from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.seleniumhq.org/")
driver.implicitly_wait(30)

download = driver.find_element_by_xpath("//a[@title='Get Selenium']")
download.send_keys(Keys.SHIFT + Keys.ENTER)
parent_window_handle = driver.current_window_handle
new_window_handle = None

handles = driver.window_handles
for handle in handles:
    if handle != parent_window_handle:
        new_window_handle = handle
        break
driver.switch_to_window(new_window_handle)
time.sleep(5)
driver.find_element_by_xpath("//a[text()='Maven users']").click()

time.sleep(5)
driver.quit()
