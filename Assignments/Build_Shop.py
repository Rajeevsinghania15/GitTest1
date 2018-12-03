from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://buildshop.com/signin?c=1")
driver.implicitly_wait(30)

driver.find_element_by_css_selector("a#ctl00_btnSignIn").click()
user = driver.find_element_by_css_selector("input#ctl00_ContentPlaceHolder1_Login101_UserName")
user.send_keys('sushma.jb82@gmail.com')
pwd = driver.find_element_by_css_selector("input#ctl00_ContentPlaceHolder1_Login101_Password")
pwd.send_keys('Qspiders$1')
driver.find_element_by_css_selector("a.signinP").click()
driver.find_element_by_css_selector("a[class='btnTopMenu'][href = '/customers/']").click()
driver.find_element_by_css_selector("input#ctl00_MainContent_btnNew").click()
company =driver.find_element_by_css_selector("input#ctl00_MainContent_FormViewContactInsert_txtContactName")
company.send_keys('Test Yantra')
job=driver.find_element_by_css_selector("input#ctl00_MainContent_FormViewContactInsert_txtTitle")
job.send_keys('Tester')
name=driver.find_element_by_css_selector("input#ctl00_MainContent_FormViewContactInsert_txtFirstName")
name.send_keys('kishore')
phone= driver.find_element_by_css_selector("input#ctl00_MainContent_FormViewContactInsert_EmailTextBox")
phone.send_keys('kishorekumar.reddi@gmail.com')
save=driver.find_element_by_css_selector("input[type='submit'][name='ctl00$MainContent$FormViewContactInsert$InsertButton']")
save.click()
driver.execute_script(" window.scrollTo(0, document.body.scrollTop)")

driver.find_element_by_css_selector("input[type='button'][name='ctl00$MainContent$btnBack']").click()

customer = driver.find_element_by_css_selector("span#ctl00_MainContent_GridView1_ctl04_lblFirstName")
print(customer.text)
if customer.is_displayed():
    print("Successfully Customer  created")
else:
    print("Customer not created")
time.sleep(5)
driver.close()