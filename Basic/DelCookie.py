from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("http://demo.actitime.com")

time.sleep(5)
cookie = {'name':'MyCookie', 'value': 'xyz'}
driver.add_cookie(cookie)

print('-----------------------------')
driver.delete_cookie('MyCookie')
print('Deleted the cookie with name: mycookie')
print('-----------------------------')
print(driver.get_cookie('MyCookie'))

driver.close()