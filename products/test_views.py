import unittest
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from django.core import management
from django.core.management.commands import loaddata


class DesktopProductViewsTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        management.call_command('flush', verbosity=0, interactive=False)
        management.call_command(
            'loaddata',
            'products/fixtures/products-data.json', verbosity=0)
        management.call_command(
            'loaddata',
            'products/fixtures/product-areas-data.json', verbosity=0)
        super().setUpClass()
        options = Options()
        options.add_argument("--headless")
        cls.driver = webdriver.Chrome(options=options)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super().tearDownClass()

    def test_all_features(self):

        self.driver.get("http://localhost:8000/products")
        self.driver.implicitly_wait(0)  # seconds

        elements = self.driver.find_elements_by_xpath(
            "//div/h3[contains(@class, 'description-heading')]")

        elements_list = []

        test = [
            'Description UI Issue',
            'Description Networking Feature',
            'Description Networking Feature',
            'Description UI Issue']

        for e in elements:
            elements_list.append(e.text)

        self.assertListEqual(elements_list, test)

        elements = self.driver.find_elements_by_xpath(
            "//li[contains(@class, 'accordion-item is-active')]")

        self.assertEqual(len(elements), 4)

# TODO: test profile view


if __name__ == '__main__':
    unittest.main(warnings='ignore')
