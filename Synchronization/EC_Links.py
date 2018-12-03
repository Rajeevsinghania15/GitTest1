from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.google.co.in")
driver.implicitly_wait(30)

links = driver.find_elements_by_tag_name("a")
print("Total links in google page is:",len(links))
print("-----------------------------------------")
for link in links:
    print(link.get_attribute("href"))
print("-----------------------------------------")

driver.close()