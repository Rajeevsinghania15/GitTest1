from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("file:///C:/Users/Abhishek/Downloads/multiSelect.html")

multiDropdown = driver.find_element(By.NAME,"Mobdevices")
select = Select(multiDropdown)
if select.is_multiple:
    print("True: Multi-select dropdown")
else:
    print("False: is not multi-select dropdown")
select.select_by_index(3)
select.select_by_value('5')
select.select_by_visible_text("iPhone")
select.deselect_by_index(3)

select.deselect_by_index(3)
time.sleep(2)
select.deselect_by_visible_text("iPhone")
time.sleep(2)
select.deselect_by_value('5')

time.sleep(5)

driver.close()