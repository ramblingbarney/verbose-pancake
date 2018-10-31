import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class SiteNavigationTest(unittest.TestCase):

    def setUp(self):
        # create selenium browser instance and options
        options = Options()
        options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=options)
        self.li_text = []

    def tearDown(self):
        self.driver.get("http://localhost:5000/logout")
        self.driver.quit()

    def test_login_navigation(self):
        ''' Test login navigation element '''

        self.driver.get("http://127.0.0.1:8000")
        self.driver.implicitly_wait(0)  # seconds

        elements = self.driver.find_elements_by_xpath(
            "//li[contains(@class, 'navigation-link')]/a")

        elements[0].click()

        self.assertEqual(
            self.driver.current_url, 'http://127.0.0.1:8000/accounts/login/')

    def test_register_navigation(self):
        ''' Test register navigation element '''

        self.driver.get("http://127.0.0.1:8000")
        self.driver.implicitly_wait(0)  # seconds

        elements = self.driver.find_elements_by_xpath(
            "//li[contains(@class, 'navigation-link')]/a")

        elements[1].click()

        self.assertEqual(
            self.driver.current_url,
            'http://127.0.0.1:8000/accounts/register/')


class SitePageElementsShownTest(unittest.TestCase):

    def setUp(self):
        # create selenium browser instance and options
        options = Options()
        options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=options)

        self.li_text = []

    def tearDown(self):
        self.driver.get("http://localhost:5000/logout")
        self.driver.quit()

    def test_home_page_elements(self):
        ''' Test home page elements (not logged in) '''

        self.driver.get("http://127.0.0.1:8000")
        self.driver.implicitly_wait(0)  # seconds

        elements = self.driver.find_elements_by_xpath(
            "//li[contains(@class, 'navigation-link')]/a")

        for element in elements:
            self.li_text.append(element.text)

        test_list = ['Login', 'Register']

        self.assertListEqual(test_list, self.li_text)

    def test_login_page_elements(self):
        ''' Test login navigation element '''

        self.driver.get("http://127.0.0.1:8000")
        self.driver.implicitly_wait(0)  # seconds

        elements = self.driver.find_elements_by_xpath(
            "//li[contains(@class, 'navigation-link')]/a")
        elements[0].click()
        self.driver.implicitly_wait(0)  # seconds

        elements = []
        elements.append(self.driver.find_element_by_id("id_username"))
        elements.append(self.driver.find_element_by_id("id_password"))
        elements.append(self.driver.find_element_by_id("id_login_button"))

        self.assertEqual(len(elements), 3)

    def test_registration_page_elements(self):
        ''' Test login navigation element '''

        self.driver.get("http://127.0.0.1:8000")
        self.driver.implicitly_wait(0)  # seconds

        elements = self.driver.find_elements_by_xpath(
            "//li[contains(@class, 'navigation-link')]/a")
        elements[1].click()
        self.driver.implicitly_wait(0)  # seconds

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
