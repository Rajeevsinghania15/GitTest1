
from selenium import webdriver

import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("file:///C:/Users/Abhishek/Downloads/alertPopUp.html")
driver.implicitly_wait(30)

driver.find_element_by_xpath("//button[text()='Try it']").click()
alert = driver.switch_to_alert
time.sleep(4)
print("Text present on the alert is ", alert.text)
alert.send_keys("Qspider")

alert.accept()
#alert.dismiss()
time.sleep(4)
driver.close()