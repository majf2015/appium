from selenium import webdriver
import os,time


PATH=lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.2'
desired_caps['deviceName'] = 'lenovo S668t'
desired_caps['app'] = PATH('E:\\appium\\app-dev-debug-mgr.apk')
desired_caps['appPackage'] = 'com.xmd.manager'
desired_caps['appActivity'] = 'com.xmd.manager.window.LoginActivity'
desired_caps['noReset'] = True

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
time.sleep(1)
driver.find_element_by_id('id/password').send_keys('999999')
time.sleep(1)
driver.find_element_by_id('id/login').click()
time.sleep(5)
driver.quit()