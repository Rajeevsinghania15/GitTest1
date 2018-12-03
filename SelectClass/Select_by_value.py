from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://airindia.com")

dropDown = driver.find_element(By.ID,"ContentPlaceHolder1_UserLanguage1_drpCountry")
listBox = Select(dropDown)
listBox.select_by_value("76")

time.sleep(5)
driver.close()