import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("file:///C:/Users/PriyaPramod/Desktop/HTML%20Pages/Practice/Slider.html")
driver.implicitly_wait(30)
sliderEle = driver.find_element_by_xpath("//span[@class='ui-slider-handle ui-state-default ui-corner-all']")
 
lastPositionSlider = driver.find_element_by_xpath("//div[@id='slider-range-max']/div[2]")
 
action = ActionChains(driver)
action.click_and_hold(sliderEle)
action.move_to_element(lastPositionSlider).pause(1)
action.move_to_element(lastPositionSlider).pause(1)
action.release(sliderEle).pause(1)
action.perform()
   
time.sleep(10)

driver.close()