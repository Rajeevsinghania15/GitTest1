from selenium import webdriver
import keyboard
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.seleniumhq.org/")
driver.implicitly_wait(30)

time.sleep(5)
keyboard.press_and_release('control+w')


