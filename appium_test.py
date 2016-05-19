from appium import webdriver
from time import sleep

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.3'
desired_caps['platformName'] = 'Android Emulator'
desired_caps['platformName'] = 'com.android.calculator2'
desired_caps['platformName'] = '.Calculator'

driver = webdriver.Remate('http://localhost:4723/wd/hub', desired_caps)
driver.find_element_by_name("1").click()
driver.find_element_by_name("5").click()
driver.find_element_by_name("9").click()
driver.find_element_by_name("delete").click()