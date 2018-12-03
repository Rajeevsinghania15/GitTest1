from selenium import webdriver
import time

user = "kumar, kishore"
driver = webdriver.Chrome()
driver.get("http://demo.actitime.com")
driver.maximize_window()
driver.implicitly_wait(30)

driver.find_element_by_css_selector("input#username").send_keys('admin')
driver.find_element_by_css_selector("input[name='pwd']").send_keys('manager')
driver.find_element_by_css_selector("a#loginButton").click()

driver.find_element_by_xpath("//div[text()='USERS']").click()

checkUsers = driver.find_elements_by_xpath("//thead[@id='userListTableHeader']/..//span[@class='userNameSpan']")
count = 0
for count in range(count,len(checkUsers)):
    driver.execute_script("arguments[0].scrollIntoView()", checkUsers[count])
    if (user == checkUsers[count].text):
        driver.find_element_by_xpath("//span[@class='userNameSpan' and contains(text(),'"+checkUsers[count].text+"')]").click()
        time.sleep(5)
        driver.find_element_by_xpath("//button[@id='userDataLightBox_deleteBtn']").click()
        
        alert = driver.switch_to.alert
        alert.accept()
        break
    count = count + 1
time.sleep(5)

driver.find_element_by_xpath("//div[contains(text(),'Add User')]").click()

driver.find_element_by_xpath("//input[@name='firstName']").send_keys('kishore')
driver.find_element_by_xpath("//input[@name='lastName']").send_keys('kumar')
driver.find_element_by_xpath("//input[@name='email']").send_keys('kishorekumar.reddi@gmail.com')

driver.find_element_by_xpath("//input[@name='username']").send_keys('kishorekumar')
driver.find_element_by_xpath("//input[@name='password']").send_keys('kishore')
driver.find_element_by_xpath("//input[@name='passwordCopy']").send_keys('kishore')

driver.find_element_by_xpath("(//span[@class='defaultGroupName'])[1]").click()
driver.find_element_by_xpath("(//span[@class='defaultGroupName'])[2]").click()

driver.find_element_by_xpath("(//div[@class=' at-dropdown-list-btn-ct'])[1]").click()
driver.find_element_by_xpath("//button[contains(text(),'March 2018')]/../../../../../../../..//span[text()='21']").click()
driver.find_element_by_xpath("//span[contains(text(),'Create User')]").click()

driver.close()
