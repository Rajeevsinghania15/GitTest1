
from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("http://demo.actitime.com")

time.sleep(10)

loginButton = driver.find_element_by_xpath("(//div[contains(text(), 'Login')])[1]")


sizeofAnEle = loginButton.size
print("Size of an element :" ,sizeofAnEle)
print("-----------------------------------")
print("Height of an element :", sizeofAnEle.get("height"))
print("Width of an element :", sizeofAnEle.get("width"))
print("------------------------------------")


time.sleep(5)
driver.close()