import time
from selenium import webdriver
from pathlib  import Path

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demo.actitime.com")
driver.implicitly_wait(30)

driver.find_element_by_name("username").send_keys("admin")
driver.find_element_by_name("pwd").send_keys("manager")
driver.find_element_by_id("loginButton").click()

driver.find_element_by_xpath("//div[text()='REPORTS']").click()
driver.find_element_by_xpath("//div[contains(text(),'Monthly Team Performance')]").click()
csv=driver.find_element_by_xpath("(//td[contains(@class,'headerFooterCell clickableCell exportToCSV cellWithBorder')])[1]")
csv.click()
file_path = Path("C:\\Users\\Abhishek\\Downloads\\actiTIME - Staff Performance (Feb 01, 2018 - Feb 28, 2018) (1).csv")
time.sleep(5)

if file_path.is_file():
    print("True: File is downloaded")
else:
    print("False: File is not downloaded")
driver.close()