from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("file:///C:/Users/Abhishek/Downloads/multiSelect.html")

multiDropdown = driver.find_element(By.NAME,"Mobdevices")
select = Select(multiDropdown)

select.select_by_index(3)
select.select_by_value('5')
select.select_by_visible_text("iPhone")

selectedOptions = select.all_selected_options

for selectedOption in selectedOptions:
    print(selectedOption.text)

time.sleep(5)

driver.close()