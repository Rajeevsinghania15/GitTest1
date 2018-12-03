from selenium import webdriver
import autoit
driver = webdriver.Firefox()
driver.get("https://www.naukri.com/")
driver.implicitly_wait(30)

driver.find_element_by_xpath("//input[@value='Upload CV']").click()

autoit.win_active("Open")
autoit.control_set_text("Open","Edit1","E:\\kishore\\add.py")
autoit.control_send("Open","Button1","{ENTER}")

driver.close()