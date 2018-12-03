
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions  as EC
from selenium.common.exceptions import TimeoutException
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("file:///C:/Users/Abhishek/Downloads/alertPopUp.html")
driver.implicitly_wait(30)

driver.find_element_by_xpath("//button[text()='Try it']")
try:
    waitFor = WebDriverWait(driver,30)
    returnValue =waitFor.until(EC.alert_is_present())
    returnValue.accept()
except TimeoutException:
    print("No alert is present !")
driver.close()