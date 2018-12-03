from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("https://www.google.co.in/?gfe_rd=cr&dcr=0&ei=s35pWt7LLImjX52-r6gL")
time.sleep(5)

driver.find_element_by_css_selector("input#lst-ib").send_keys('selenium')

time.sleep(5)
driver.find_element_by_css_selector("ul[role='listbox'] > li:nth-child(5)").click()
time.sleep(5)


driver.close()