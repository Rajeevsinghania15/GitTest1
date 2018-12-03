from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("path of the link")
time.sleep(10)
driver.find_element_by_link_text('msg3').click()
time.sleep(5)
driver.close()