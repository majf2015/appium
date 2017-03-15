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
        self.tv_data = dict(conf.items('Tv'))

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

    def test_tv_data(self):
        self.test_login()
        WebDriverWait(self.driver, 50).until(expected_conditions.visibility_of_element_located
                                             ((By.XPATH, "//android.widget.TextView[contains(@resource-id,'tv_wifi_today')]")))
        tv_wifi_today = self.driver.find_element_by_xpath\
            ("//android.widget.TextView[contains(@resource-id,'tv_wifi_today')]").text
        if tv_wifi_today == self.tv_data['tv_wifi_today']:
            print 'tv_wifi_today data right'
        else:
            raise Exception('error:tv_wifi_today ')

        tv_wifi_accumulate = self.driver.find_element_by_xpath\
            ("//android.widget.TextView[contains(@resource-id,'tv_wifi_accumulate')]").text
        if tv_wifi_accumulate == self.tv_data['tv_wifi_accumulate']:
            print 'tv_wifi_accumulate data right'
        else:
            raise Exception('error:tv_wifi_accumulate ')

        tv_visit_today = self.driver.find_element_by_xpath\
            ("//android.widget.TextView[contains(@resource-id,'tv_visit_today')]").text
        if tv_visit_today == self.tv_data['tv_visit_today']:
            print 'tv_visit_today data right'
        else:
            raise Exception('error:tv_visit_today ')

        tv_visit_accumulate = self.driver.find_element_by_xpath\
            ("//android.widget.TextView[contains(@resource-id,'tv_visit_accumulate')]").text
        if tv_visit_accumulate == self.tv_data['tv_visit_accumulate']:
            print 'tv_visit_accumulate data right'
        else:
            raise Exception('error:tv_visit_accumulate ')

        tv_new_register_today = self.driver.find_element_by_xpath\
            ("//android.widget.TextView[contains(@resource-id,'tv_new_register_today')]").text
        if tv_new_register_today == self.tv_data['tv_new_register_today']:
            print 'tv_new_register_today data right'
        else:
            raise Exception('error:tv_new_register_today ')

        tv_new_register_accumulate = self.driver.find_element_by_xpath\
            ("//android.widget.TextView[contains(@resource-id,'tv_new_register_accumulate')]").text
        if tv_new_register_accumulate == self.tv_data['tv_new_register_accumulate']:
            print 'tv_new_register_accumulate data right'
        else:
            raise Exception('error:tv_new_register_accumulate ')

        tv_coupon_get_today = self.driver.find_element_by_xpath\
            ("//android.widget.TextView[contains(@resource-id,'tv_coupon_get_today')]").text
        if tv_coupon_get_today == self.tv_data['tv_coupon_get_today']:
            print 'tv_coupon_get_today data right'
        else:
            raise Exception('error:tv_coupon_get_today ')

        tv_coupon_get_accumulate = self.driver.find_element_by_xpath\
            ("//android.widget.TextView[contains(@resource-id,'tv_coupon_get_accumulate')]").text
        if tv_coupon_get_accumulate == self.tv_data['tv_coupon_get_accumulate']:
            print 'tv_coupon_get_accumulate data right'
        else:
            raise Exception('error:tv_coupon_get_accumulate ')

        tv_accepted_order_count = self.driver.find_element_by_xpath\
            ("//android.widget.TextView[contains(@resource-id,'tv_accepted_order_count')]").text
        if tv_accepted_order_count == self.tv_data['tv_accepted_order_count']:
            print 'tv_accepted_order_count data right'
        else:
            raise Exception('error:tv_accepted_order_count ')

        tv_pending_order_count = self.driver.find_element_by_xpath\
            ("//android.widget.TextView[contains(@resource-id,'tv_pending_order_count')]").text
        if tv_pending_order_count == self.tv_data['tv_pending_order_count']:
            print 'tv_pending_order_count data right'
        else:
            raise Exception('error:tv_pending_order_count ')

        tv_completed_order_count = self.driver.find_element_by_xpath\
            ("//android.widget.TextView[contains(@resource-id,'tv_completed_order_count')]").text
        if tv_completed_order_count == self.tv_data['tv_completed_order_count']:
            print 'tv_completed_order_count data right'
        else:
            raise Exception('error:tv_completed_order_count ')