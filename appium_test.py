from selenium import webdriver
import os,time


PATH=lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.2'
desired_caps['deviceName'] = 'lenovo S668t'
desired_caps['app'] = PATH('E:\\appium\\9358mgr_v3.7.0.42_dev_xiaomodo_201702081651.apk')
desired_caps['appPackage'] = 'com.xmd.manager'
desired_caps['appActivity'] = 'com.xmd.manager.window.LoginActivity'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
time.sleep(5)
driver.find_element_by_id('com.xmd.manager:id/login').click()
time.sleep(5)
driver.quit()