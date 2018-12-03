import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("file:///C:/Users/PriyaPramod/Desktop/HTML%20Pages/Practice/Slider.html")
driver.implicitly_wait(30)
sliderEle = driver.find_element_by_xpath("//span[@class='ui-slider-handle ui-state-default ui-corner-all']")
    
i = 0

for i in range(i, 3):
    sliderEle.send_keys(Keys.ARROW_RIGHT)
    i = i + 1
    time.sleep(2)

driver.close()