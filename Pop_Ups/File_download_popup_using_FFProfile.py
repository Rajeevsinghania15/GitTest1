from selenium import webdriver
import time

profile = webdriver.FirefoxProfile()
profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "Application/zip")
#download into desktop
profile.set_preference("browser.download.folderList",0)
#download into specific folder
'''
profile.set_preference("browser.download.folderList",2)
profile.set_preference("browser.download.dir", "E:\\") 
'''
driver = webdriver.Firefox(profile)
driver.maximize_window()
driver.get("https://www.seleniumhq.org/download/")
driver.implicitly_wait(30)

driver.find_element_by_xpath("//td[text()='Java']/..//a[text()='Download']").click()

time.sleep(5)