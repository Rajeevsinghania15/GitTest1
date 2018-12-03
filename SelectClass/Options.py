from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("file:///C:/Users/Abhishek/Downloads/multiSelect.html")

multiDropdown = driver.find_element(By.NAME,"Mobdevices")
select = Select(multiDropdown)


allOptions = select.options

for option in allOptions:
    print(option.text)

time.sleep(5)

driver.close()