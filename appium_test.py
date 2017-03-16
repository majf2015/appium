import unittest,public_module
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


class AppTest(unittest.TestCase):
    def setUp(self):
        self.public = public_module.Public()
        self.public.login()
        self.conf = self.public.conf
        self.project_path = self.public.current_path
        self.driver = self.public.driver
        self.debug = self.public.debug

        self.tv_data = dict(self.conf.items('Tv'))

    def tearDown(self):
        self.driver.quit()

    def test_tv_data(self):
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