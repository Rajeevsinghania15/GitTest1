from selenium import webdriver
import time
from PIL import Image
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demo.actitime.com/login.do")
driver.implicitly_wait(30)

ele = driver.find_element_by_id("loginButton")
driver.save_screenshot("Sample.png")
img = Image.open("Sample.png")

loc = ele.location
size = ele.size

left = loc["x"]
top = loc['y']
right = loc["x"] + size['width']
bottom = loc['y'] + size['height']

img = img.crop((left,top,right,bottom))
img.save('Cropping.png')

time.sleep(5)
driver.close()