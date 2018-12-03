import unittest
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from django.core import management
from django.core.management.commands import loaddata


class DesktopProductFeaturesIssuesTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        management.call_command('flush', verbosity=0, interactive=False)
        management.call_command(
            'loaddata',
            'products/fixtures/products-data.json', verbosity=0)
        management.call_command(
            loaddata.Command(),
            'products/fixtures/products-data.json', verbosity=0)
        super().setUpClass()
        options = Options()
        options.add_argument("--headless")
        cls.driver = webdriver.Chrome(options=options)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super().tearDownClass()


    def test_add_new_feature(self):

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

        self.driver.get("http://localhost:8000/products/new")
        self.driver.implicitly_wait(0)  # seconds

        self.driver.find_element_by_id('id_name').send_keys('Product 3')
        self.driver.find_element_by_id('id_description').send_keys('Product Description')
        self.driver.find_element_by_id('id_price').send_keys('3')

        select = Select(self.driver.find_element_by_id('id_product_area'))
        select.select_by_visible_text('Networking')
        select = Select(self.driver.find_element_by_id('id_product_need'))
        select.select_by_visible_text('Medium')
        select = Select(self.driver.find_element_by_id('id_product_complexity'))
        select.select_by_visible_text('Medium')
        select = Select(self.driver.find_element_by_id('id_status'))
        select.select_by_visible_text('Doing')
        select = Select(self.driver.find_element_by_id('id_product_type'))
        select.select_by_visible_text('Feature')

        self.driver.find_element_by_id(
            'id_image').send_keys(
                os.getcwd()+'/products/fixtures/IMG_4496.JPG')
        self.driver.find_element_by_id(
            'id_product_document').send_keys(
                os.getcwd() + '/products/fixtures/small_sharp_tools_pragprog_connections.pdf')

        self.driver.find_element_by_xpath("//*[contains(text(), 'Save')]").click()

        self.driver.get("http://localhost:8000/products")
        self.driver.implicitly_wait(0)  # seconds

        elements = self.driver.find_elements_by_xpath(
            "//li[contains(@class, 'accordion-item is-active')]")

        self.assertEqual(len(elements), 3)

    def test_add_new_issue(self):

        self.driver.get("http://localhost:8000/products/new")
        self.driver.implicitly_wait(0)  # seconds

        self.driver.find_element_by_id('id_name').send_keys('Product 4')
        self.driver.find_element_by_id('id_description').send_keys('Product Description')
        self.driver.find_element_by_id('id_price').send_keys('4')

        select = Select(self.driver.find_element_by_id('id_product_area'))
        select.select_by_visible_text('UI')
        select = Select(self.driver.find_element_by_id('id_product_need'))
        select.select_by_visible_text('Low')
        select = Select(self.driver.find_element_by_id('id_product_complexity'))
        select.select_by_visible_text('Low')
        select = Select(self.driver.find_element_by_id('id_status'))
        select.select_by_visible_text('To Do')
        select = Select(self.driver.find_element_by_id('id_product_type'))
        select.select_by_visible_text('Issue')

        self.driver.find_element_by_id(
            'id_image').send_keys(
                os.getcwd()+'/products/fixtures/IMG_4496.JPG')
        self.driver.find_element_by_id(
            'id_product_document').send_keys(
                os.getcwd() + '/products/fixtures/small_sharp_tools_pragprog_connections.pdf')

        self.driver.find_element_by_xpath("//*[contains(text(), 'Save')]").click()

        self.driver.get("http://localhost:8000/products")
        self.driver.implicitly_wait(0)  # seconds

        elements = self.driver.find_elements_by_xpath(
            "//li[contains(@class, 'accordion-item is-active')]")

        self.assertEqual(len(elements), 4)


if __name__ == '__main__':
    unittest.main(warnings='ignore')
