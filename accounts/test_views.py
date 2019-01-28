import unittest
import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.remote_connection import LOGGER




class DesktopNavigationTest(unittest.TestCase):

    def setUp(self):
        # create selenium browser instance and options
        LOGGER.setLevel(logging.WARNING)
        options = Options()
        options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=options)
        self.driver.set_window_position(0, 0)
        self.driver.set_window_size(1366, 668)
        self.li_text = []

    def tearDown(self):
        self.driver.quit()

    def test_login_navigation_desktop(self):

        self.driver.get("http://localhost:8000")
        self.driver.implicitly_wait(0)  # seconds

        self.driver.find_element_by_xpath(
            "//i[contains(@class, 'fa-sign-in-alt')]").click()

        self.assertEqual(
            self.driver.current_url, 'http://localhost:8000/accounts/login/')

    def test_register_navigation(self):

        self.driver.get("http://localhost:8000")
        self.driver.implicitly_wait(0)  # seconds

        self.driver.find_element_by_id('desktop-menu').click()

        self.driver.implicitly_wait(0)  # seconds

        self.driver.find_element_by_xpath(
            "//div/a[contains(text(), 'Register')]").click()

        self.assertEqual(
            self.driver.current_url,
            'http://localhost:8000/accounts/register/')

    def test_features_issues_navigation(self):

        self.driver.get("http://localhost:8000")
        self.driver.implicitly_wait(0)  # seconds

        self.driver.find_element_by_id('desktop-menu').click()

        self.driver.implicitly_wait(0)  # seconds

        self.driver.find_element_by_xpath(
            "//div/a[contains(text(), 'Features & Issues')]").click()

        self.assertEqual(
            self.driver.current_url,
            'http://localhost:8000/products/')


class MobileNavigationTest(unittest.TestCase):

    def setUp(self):
        # create selenium browser instance and options
        LOGGER.setLevel(logging.WARNING)
        options = Options()
        options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=options)
        self.driver.set_window_position(0, 0)
        self.driver.set_window_size(500, 668)
        self.li_text = []

    def tearDown(self):
        self.driver.quit()

    def test_mobile_navigation(self):

        self.driver.get("http://localhost:8000")
        self.driver.implicitly_wait(0)  # seconds

        self.driver.find_element_by_id('mobile-menu').click()

        self.driver.implicitly_wait(0)  # seconds

        self.assertEqual(1, 1)


class SitePageElementsShownTest(unittest.TestCase):

    def setUp(self):
        # create selenium browser instance and options
        LOGGER.setLevel(logging.WARNING)
        options = Options()
        options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=options)

        self.li_text = []

    def tearDown(self):
        self.driver.quit()

    def test_login_page_elements(self):

        self.driver.get("http://localhost:8000")
        self.driver.implicitly_wait(0)  # seconds

        self.driver.find_element_by_xpath(
            "//i[contains(@class, 'fa-sign-in-alt')]").click()

        elements = []
        elements.append(self.driver.find_element_by_id("id_username"))
        elements.append(self.driver.find_element_by_id("id_password"))
        elements.append(self.driver.find_element_by_id("id_login_button"))

        self.assertEqual(len(elements), 3)

    def test_registration_page_elements(self):

        self.driver.get("http://localhost:8000")
        self.driver.implicitly_wait(0)  # seconds

        self.driver.find_element_by_id('desktop-menu').click()

        self.driver.implicitly_wait(0)  # seconds

        self.driver.find_element_by_xpath(
            "//div/a[contains(text(), 'Register')]").click()

        elements = []
        elements.append(self.driver.find_element_by_id("id_username"))
        elements.append(self.driver.find_element_by_id("id_email"))
        elements.append(self.driver.find_element_by_id("id_password1"))
        elements.append(self.driver.find_element_by_id("id_password2"))
        elements.append(self.driver.find_element_by_id("id_register_button"))

        self.assertEqual(len(elements), 5)


if __name__ == '__main__':
    unittest.main(warnings='ignore')


# TODO: test profile view
