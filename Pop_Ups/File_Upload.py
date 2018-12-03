from selenium import webdriver
#import os
import autoit
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("path of the file")
driver.implicitly_wait(30)

file_link = driver.find_element_by_id("fileselect")
file_link.click()
time.sleep(5)
#os.startfile("E:\\kishore\\AutoIT\\Fileupload.exe")
autoit.win_active("Open")
autoit.control_set_text("Open","Entering the value to the edit box","Edit1","C:\Users\Abhishek\eclipse-workspace\Selenium\JavaScriptExecutor\EnterText.py")
autoit.control_send("Open","Button1","{ENTER}")

file_name = driver.find_element_by_xpath("//div[@id='messages']//strong[1]")

if file_name.text == "EnterText.py":
    print("File is uploaded")
else:
    print("File is not uploaded")

driver.close()