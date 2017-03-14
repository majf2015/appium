import os, sys,time,unittest, ConfigParser
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


class AppTest(unittest.TestCase):
    def setUp(self):
        current_path = sys.path[0]
        conf = ConfigParser.ConfigParser()
        conf.read(os.path.join(current_path,'config.conf'))
        desired_cap = dict(conf.items('desired_cap'))
        PATH=lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))

        desired_caps = {}
        desired_caps['platformName'] = desired_cap['platformname']
        desired_caps['platformVersion'] = desired_cap['platformversion']
        desired_caps['deviceName'] = desired_cap['devicename']
        desired_caps['app'] = PATH(desired_cap['app'])
        desired_caps['appPackage'] = desired_cap['apppackage']
        desired_caps['appActivity'] = desired_cap['appactivity']
        desired_caps['noReset'] = desired_cap['noreset']

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.account = dict(conf.items('ManagerAccount'))

    def tearDown(self):
        self.driver.quit()


    def test_login(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located
                                            ((By.XPATH, "//android.widget.EditText[contains(@resource-id,'username')]")))
        self.driver.find_element_by_xpath("//android.widget.EditText[contains(@resource-id,'username')]").clear()
        self.driver.find_element_by_xpath("//android.widget.EditText[contains(@resource-id,'username')]")\
            .send_keys(self.account['user'])
        self.driver.find_element_by_xpath("//android.widget.EditText[contains(@resource-id,'password')]")\
            .send_keys(self.account['password'])
        self.driver.find_element_by_xpath("//android.widget.Button[contains(@resource-id,'login')]").click()

