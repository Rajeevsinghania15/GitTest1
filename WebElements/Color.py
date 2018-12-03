
from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("http://demo.actitime.com")

time.sleep(10)

loginButton = driver.find_element_by_xpath("(//div[contains(text(), 'Login')])[1]")

colorOfAnEle = loginButton.value_of_css_property('color')
fontSizeOfAnEle = loginButton.value_of_css_property('font-size')

print("Color of an Element is :",colorOfAnEle)
print("----------------------------------------")
print("Font size of an Element is :",fontSizeOfAnEle)

time.sleep(5)
driver.close()