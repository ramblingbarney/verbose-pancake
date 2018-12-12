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
        super().setUpClass()
        options = Options()
        options.add_argument("--headless")
        cls.driver = webdriver.Chrome(options=options)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super().tearDownClass()

    def test_add_new_feature_without_image_or_document(self):

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
        self.driver.find_element_by_id(
            'id_description').send_keys('Product Description')
        self.driver.find_element_by_id('id_price').send_keys('3')

        Select(self.driver.find_element_by_id(
            'id_product_area')).select_by_visible_text('Networking')
        Select(self.driver.find_element_by_id(
            'id_product_need')).select_by_visible_text('Medium')
        Select(self.driver.find_element_by_id(
            'id_product_complexity')).select_by_visible_text('Medium')
        Select(self.driver.find_element_by_id(
            'id_status')).select_by_visible_text('Doing')
        Select(self.driver.find_element_by_id(
            'id_product_type')).select_by_visible_text('Feature')

        self.driver.find_element_by_xpath(
            "//*[contains(text(), 'Save')]").click()

        self.driver.get("http://localhost:8000/products")
        self.driver.implicitly_wait(0)  # seconds

        elements = self.driver.find_elements_by_xpath(
            '//div[@class="image-detail"]//img[@src]')

        image_src = elements[2].get_attribute('src')

        self.assertEqual(image_src, 'http://localhost:8000/media/images/image_placeholder.jpeg')

        elements = self.driver.find_elements_by_xpath(
            "//span[@class='file-name']")

        self.assertEqual(elements[2].text, '')

        elements = self.driver.find_elements_by_xpath(
            "//li[contains(@class, 'accordion-item is-active')]")

        self.assertEqual(len(elements), 3)

    def test_add_new_issue(self):

        self.driver.get("http://localhost:8000/products/new")
        self.driver.implicitly_wait(0)  # seconds

        self.driver.find_element_by_id('id_name').send_keys('Product 4')
        self.driver.find_element_by_id(
            'id_description').send_keys('Product Description')
        self.driver.find_element_by_id('id_price').send_keys('4')

        Select(self.driver.find_element_by_id(
            'id_product_area')).select_by_visible_text('UI')
        Select(self.driver.find_element_by_id(
            'id_product_need')).select_by_visible_text('Low')
        Select(self.driver.find_element_by_id(
            'id_product_complexity')).select_by_visible_text('Low')
        Select(self.driver.find_element_by_id(
            'id_status')).select_by_visible_text('To Do')
        Select(self.driver.find_element_by_id(
            'id_product_type')).select_by_visible_text('Issue')

        self.driver.find_element_by_id(
            'id_image').send_keys(
                os.getcwd()+'/products/fixtures/IMG_4496.JPG')
        self.driver.find_element_by_id(
            'id_product_document').send_keys(
                os.getcwd() + '/products/fixtures/small_sharp_tools_pragprog_connections.pdf')

        self.driver.find_element_by_xpath(
            "//*[contains(text(), 'Save')]").click()

        self.driver.get("http://localhost:8000/products")
        self.driver.implicitly_wait(0)  # seconds

        elements = self.driver.find_elements_by_xpath(
            "//li[contains(@class, 'accordion-item is-active')]")

        self.assertEqual(len(elements), 4)

    def test_add_new_form_validation_error(self):

        self.driver.get("http://localhost:8000/products/new")
        self.driver.implicitly_wait(0)  # seconds

        self.driver.find_element_by_id('id_name').send_keys('Product 2')
        self.driver.find_element_by_id(
            'id_description').send_keys('Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?')
        self.driver.find_element_by_id('id_price').send_keys('20.00')

        Select(self.driver.find_element_by_id(
            'id_product_area')).select_by_visible_text('Networking')
        Select(self.driver.find_element_by_id(
            'id_product_need')).select_by_visible_text('Medium')
        Select(self.driver.find_element_by_id(
            'id_product_complexity')).select_by_visible_text('Medium')
        Select(self.driver.find_element_by_id(
            'id_status')).select_by_visible_text('Complete')
        Select(self.driver.find_element_by_id(
            'id_product_type')).select_by_visible_text('Feature')

        self.driver.find_element_by_id(
            'id_image').send_keys(
                os.getcwd()+'/products/fixtures/startbootstrap-sb-admin-gh-pages.zip')
        self.driver.find_element_by_id(
            'id_product_document').send_keys(
                os.getcwd() + '/products/fixtures/cityam-2018-06-28-5b341f418bcd3.pdf')

        self.driver.find_element_by_xpath(
            "//*[contains(text(), 'Save')]").click()

        element = self.driver.find_element_by_xpath(
            "//ul[contains(@class, 'errorlist')]")

        warnings_list = '<li>name<ul class="errorlist"><li>Name must be unique</li></ul></li><li>image<ul class="errorlist"><li>Upload a valid image. The file you uploaded was either not an image or a corrupted image.</li></ul></li><li>product_document<ul class="errorlist"><li>Please keep filesize under 5.0&nbsp;MB. Current filesize 15.6&nbsp;MB</li></ul></li>'

        self.assertEqual(element.get_attribute('innerHTML'), warnings_list)

    def test_edit_feature_name(self):

        self.driver.get("http://localhost:8000/products/edit/5")
        self.driver.implicitly_wait(0)  # seconds

        self.driver.find_element_by_id('id_name').send_keys('2')

        self.driver.find_element_by_xpath(
            "//*[contains(text(), 'Save')]").click()
        self.driver.implicitly_wait(0)  # seconds

        element = self.driver.find_element_by_xpath(
            "//a[contains(@class, 'accordion-title issue')]")

        self.assertEqual(element.text, 'Name: Product 12 Price: 10.00 Total Cumulative Donations: 10.00 Status: Doing')

        element = self.driver.find_element_by_xpath(
            '//div[@class="image-detail"]//img[@src]')

        image_src = element.get_attribute('src')

        self.assertEqual(image_src, 'http://localhost:8000/media/images/Conor_B_m8JZBno.jpg')

        element = self.driver.find_element_by_xpath(
            "//span[@class='file-name']")

        self.assertEqual(
            element.text, 'product_documents/Python_Tricks_Sample.pdf')

    def test_edit_no_change_error_name(self):

        self.driver.get("http://localhost:8000/products/edit/5")
        self.driver.implicitly_wait(0)  # seconds

        self.driver.find_element_by_xpath(
            "//*[contains(text(), 'Save')]").click()

        elements = self.driver.find_element_by_xpath(
            "//ul[contains(@class, 'errorlist')]")

        warnings_list = '<li>Name must be unique</li>'

        self.assertEqual(elements.get_attribute('innerHTML'), warnings_list)


if __name__ == '__main__':
    unittest.main(warnings='ignore')
