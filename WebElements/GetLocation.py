
from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("http://demo.actitime.com")

time.sleep(10)

loginButton = driver.find_element_by_xpath("(//div[contains(text(), 'Login')])[1]")
loc = loginButton.location

print("Co-ordinate value of Login Button is :", loc)
print(" X- Coordinate is:", loc.get("x"))
print(" Y- Coordinate is", loc.get('y'))

time.sleep(5)
driver.close()