
from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("http://www.orangecrm.com/")
time.sleep(10)

current_Title = driver.title
print(current_Title)
if('CRM Web Based Enterprise Solution' in current_Title):
    print('launched the application')
else:
    print('unable to launch the application')
print("------------------------------------------------------------------------")   
driver.find_element_by_xpath("(//a[contains(@href,'/modules.php')])[1]").click()
content = driver.find_element_by_xpath("(//div[contains(@class,'col-md-6')])[2]")

print(content.text)
print("-------------------------------------------------------------------------")

driver.find_element_by_xpath("(//b[contains(@class,'caret')])[1]").click()
time.sleep(2)
driver.find_element_by_xpath("(//a[@href='/orange-message.php'])[1]").click()
#driver.find_element_by_xpath("//ul[contains(@class,'dropdown-menu')]/li[7]").click()
time.sleep(5)

driver.close()
