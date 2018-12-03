from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("http://demo.actitime.com")

time.sleep(5)
cookie = {'name':'MyCookie', 'value': 'xyz'}
driver.add_cookie(cookie)

print('-----------------------------')
driver.delete_all_cookies()
print('Deleting all the cookies')
print('-----------------------------')
cookies = driver.get_cookies()

for cookie in cookies:
    print(cookie)
else:
    print('NO Cookies')

driver.close()