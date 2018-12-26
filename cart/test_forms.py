import unittest
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from django.core import management
from django.core.management.commands import loaddata


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

    def test_add_features_issues_cart(self):

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

        self.assertEqual(element.text, '1')

        self.driver.implicitly_wait(0)  # seconds

        element = self.driver.find_element_by_id('quantity_6')

        self.driver.execute_script("$('#quantity_6').val('1');", element)

        button = self.driver.find_element_by_id('add_to_cart_6')

        self.driver.execute_script("$('#add_to_cart_6').click();", button)
        self.driver.implicitly_wait(0)  # seconds

        element = self.driver.find_element_by_xpath(
            "//i[contains(@class, 'fa-shopping-cart')]")

        self.assertEqual(element.text, '2')


if __name__ == '__main__':
    unittest.main(warnings='ignore')
