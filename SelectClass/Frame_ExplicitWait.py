from selenium import webdriver

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()

driver.get("https://www.seleniumhq.org/")
driver.maximize_window()
driver.implicitly_wait(30)

driver.find_element_by_xpath("//a[@title='Get Selenium']").click()
driver.find_element_by_link_text("Javadoc").click()
frameEle = driver.find_element_by_xpath("//frame[@src='overview-summary.html']")

waitFor = WebDriverWait(driver,30)
response = waitFor.until(EC.frame_to_be_available_and_switch_to_it(frameEle))
driver.find_element_by_xpath("(//a[text()='Frames'])[1]").click()


driver.close()