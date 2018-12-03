
from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("http://demo.actitime.com")
time.sleep(10)
current_Title = driver.title
print(current_Title)
if('actiTIME' in current_Title):
    print('launched the application')
else:
    print('unable to launch the application')

driver.close()