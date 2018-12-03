from selenium import webdriver
#from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("file:///C:/Users/Abhishek/Downloads/Slider.html")

driver.implicitly_wait(30)
drag = driver.find_element_by_xpath("//span[@class='ui-slider-handle ui-state-default ui-corner-all']")
#action = ActionChains(driver)
count = 1
for count in range(count,10):
    drag.send_keys(Keys.ARROW_RIGHT)
    count = count + 1
#action.move_to_element(drag)
#action.click_and_hold(drag).release(drag).perform()


driver.close()