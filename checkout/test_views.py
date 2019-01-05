import unittest
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from django.core import management
from django.core.management.commands import loaddata
from datetime import datetime

this_month = datetime.now().month
next_month = datetime.now().month + 1
current_year = datetime.now().year

class DesktopCartFeaturesIssuesTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        management.call_command('flush', verbosity=0, interactive=False)
        management.call_command(
            'loaddata',
            'products/fixtures/products-data.json', verbosity=0)
        super().setUpClass()
        options = Options()
        options.add_argument("--headless")
        cls.driver = webdriver.Chrome(options=options)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super().tearDownClass()

    def test_features_cart_checkout_creditcard_number_error(self):

        self.driver.get("http://localhost:8000")
        self.driver.implicitly_wait(0)  # seconds

        self.driver.find_element_by_xpath(
            "//i[contains(@class, 'fa-sign-in-alt')]").click()
        self.driver.implicitly_wait(0)  # seconds

        self.driver.find_element_by_id(
            'id_username').send_keys('conor@conor.com')
        self.driver.find_element_by_id(
            'id_password').send_keys('example1aslkfjlksjflaf')
        self.driver.find_element_by_id(
            'id_login_button').click()

        self.driver.implicitly_wait(0)  # seconds

        self.driver.get("http://localhost:8000/products")

        self.driver.implicitly_wait(0)  # seconds

        element = self.driver.find_element_by_id('quantity_5')

        self.driver.execute_script("$('#quantity_5').val('1');", element)

        button = self.driver.find_element_by_id('add_to_cart_5')

        self.driver.execute_script("$('#add_to_cart_5').click();", button)
        self.driver.implicitly_wait(0)  # seconds

        element = self.driver.find_element_by_xpath(
            "//i[contains(@class, 'fa-shopping-cart')]")

        element.click()

        self.driver.implicitly_wait(0)  # seconds

        self.driver.find_element_by_xpath(
            "//*[contains(text(), 'Checkout')]").click()
        self.driver.implicitly_wait(0)  # seconds

        self.driver.find_element_by_id(
            'creditcard-number').send_keys('4242 4242 4242 4242d')
        self.driver.implicitly_wait(0)  # seconds

        Select(self.driver.find_element_by_id(
            'id_expiration_0')).select_by_visible_text(str(next_month))

        Select(self.driver.find_element_by_id(
            'id_expiration_1')).select_by_visible_text(str(current_year))

        self.driver.find_element_by_id('id_cvc').send_keys('123')
        self.driver.implicitly_wait(0)  # seconds

        self.driver.find_element_by_id('pay-with-creditcard').click()
        self.driver.implicitly_wait(5)  # seconds

        text_list = "Please enter in a valid credit card number."

        element = self.driver.find_element_by_xpath(
            "//*[contains(text(), 'Please enter in a valid credit card number.')]")

        self.assertEqual(element.get_attribute('innerHTML'), text_list)

        self.driver.find_element_by_xpath(
            "//i[contains(@class, 'fa-sign-out-alt')]").click()

# TODO: add test in feb 2019
    # def test_features_cart_checkout_expire_month_error(self):
    #
    #     self.driver.get("http://localhost:8000")
    #     self.driver.implicitly_wait(0)  # seconds
    #
    #     self.driver.find_element_by_xpath(
    #         "//i[contains(@class, 'fa-sign-in-alt')]").click()
    #     self.driver.implicitly_wait(0)  # seconds
    #
    #     self.driver.find_element_by_id(
    #         'id_username').send_keys('conor@conor.com')
    #     self.driver.find_element_by_id(
    #         'id_password').send_keys('example1aslkfjlksjflaf')
    #     self.driver.find_element_by_id(
    #         'id_login_button').click()
    #
    #     self.driver.implicitly_wait(0)  # seconds
    #
    #     self.driver.get("http://localhost:8000/products")
    #
    #     self.driver.implicitly_wait(0)  # seconds
    #
    #     element = self.driver.find_element_by_id('quantity_5')
    #
    #     self.driver.execute_script("$('#quantity_5').val('1');", element)
    #
    #     button = self.driver.find_element_by_id('add_to_cart_5')
    #
    #     self.driver.execute_script("$('#add_to_cart_5').click();", button)
    #     self.driver.implicitly_wait(0)  # seconds
    #
    #     element = self.driver.find_element_by_xpath(
    #         "//i[contains(@class, 'fa-shopping-cart')]")
    #
    #     element.click()
    #
    #     self.driver.implicitly_wait(0)  # seconds
    #
    #     self.driver.find_element_by_xpath(
    #         "//*[contains(text(), 'Checkout')]").click()
    #     self.driver.implicitly_wait(0)  # seconds
    #
    #     self.driver.find_element_by_id(
    #         'creditcard-number').send_keys('4242 4242 4242 4242')
    #     self.driver.implicitly_wait(0)  # seconds
    #
    #     Select(self.driver.find_element_by_id(
    #         'id_expiration_0')).select_by_visible_text(str(this_month))
    #
    #     Select(self.driver.find_element_by_id(
    #         'id_expiration_1')).select_by_visible_text(str(current_year))
    #
    #     self.driver.find_element_by_id('id_cvc').send_keys('123')
    #     self.driver.implicitly_wait(0)  # seconds
    #
    #     self.driver.find_element_by_id('pay-with-creditcard').click()
    #     self.driver.implicitly_wait(5)  # seconds
    #
    #     text_list = "The expiration date you entered is in the past."
    #
    #     element = self.driver.find_element_by_xpath(
    #         "//*[contains(text(), 'The expiration date you entered is in the past.')]")
    #
    #     self.assertEqual(element.get_attribute('innerHTML'), text_list)
    #
    #     self.driver.find_element_by_xpath(
    #         "//i[contains(@class, 'fa-sign-out-alt')]").click()


if __name__ == '__main__':
    unittest.main(warnings='ignore')
