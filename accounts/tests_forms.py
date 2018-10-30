from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.contrib.sessions.models import Session
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from django.core import management
from django.core.management.commands import loaddata
import time

timeout = time.time() + 60*1  # 1 minutes from now

class SiteLoginLogout(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        management.call_command('flush', verbosity=0, interactive=False)
        management.call_command(
            'loaddata',
            'accounts/fixtures/users-data.json', verbosity=0)
        management.call_command(
            loaddata.Command(),
            'accounts/fixtures/users-data.json', verbosity=0)
        super().setUpClass()
        options = Options()
        options.add_argument("--headless")
        cls.driver = webdriver.Chrome(options=options)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super().tearDownClass()

    def test_failed_login_form(self):

        # driver = self.driver.get("http://localhost:8000")
        # timeout = 10

        # self.driver.implicitly_wait(10)  # seconds

        self.driver.get("http://localhost:8000")

        while True:
            navigation_click = 0
            elements = self.driver.find_elements_by_xpath(
                "//li[contains(@class, 'navigation-link')]/a")
            if navigation_click == 10 or time.time() > timeout or elements:
                break
            navigation_click = navigation_click + 1

        elements[0].click()

        self.assertEqual(
            self.driver.current_url, 'http://localhost:8000/accounts/login/')

        while True:
            enter_login_details = 0

            element = self.driver.find_element_by_id('id_username')

            self.driver.find_element_by_id(
                'id_username').send_keys('conorXXXXX@conor.com')
            self.driver.find_element_by_id(
                'id_password').send_keys('example1aslkfjlksjflaf')
            self.driver.find_element_by_id(
                'id_login_button').click()

            if enter_login_details == 10 or time.time() > timeout or element:
                break
            enter_login_details = enter_login_details + 1

        # self.driver.implicitly_wait(0)  # seconds

        # self.driver.find_element_by_id(
        #     'id_username').send_keys('conorXXXXX@conor.com')
        # self.driver.find_element_by_id(
        #     'id_password').send_keys('example1aslkfjlksjflaf')
        # self.driver.find_element_by_id(
        #     'id_login_button').click()
        # self.driver.implicitly_wait(0)  # seconds
        #

        while True:
            error_text = 0

            elements_count = self.driver.find_elements_by_xpath(
                "//*[contains(text(), 'Your username or password is incorrect')]")

            if error_text == 10 or time.time() > timeout or elements_count:
                break
            error_text = error_text + 1

        self.assertEqual(len(elements_count), 1)

    def test_register_duplicate_email_form(self):

        self.driver.get("http://localhost:8000")
        self.driver.implicitly_wait(0)  # seconds

        elements = self.driver.find_elements_by_xpath(
            "//li[contains(@class, 'navigation-link')]/a")

        elements[1].click()

        self.driver.implicitly_wait(1)  # seconds

        self.driver.find_element_by_id(
            'id_email').send_keys('conor@conor.com')
        self.driver.find_element_by_id(
            'id_username').send_keys('conor2w')
        self.driver.find_element_by_id(
            'id_password1').send_keys('example1aslkfjlksjflaf')
        self.driver.find_element_by_id(
            'id_password2').send_keys('example1aslkfjlksjflaf')
        self.driver.find_element_by_id(
            'id_register_button').click()
        self.driver.implicitly_wait(0)  # seconds

        elements_count = self.driver.find_elements_by_xpath("//*[contains(text(), 'Email address must be unique')]")

        self.assertEqual(len(elements_count), 1)

    def test_register_duplicate_user_form(self):

        self.driver.get("http://localhost:8000")
        self.driver.implicitly_wait(0)  # seconds

        elements = self.driver.find_elements_by_xpath(
            "//li[contains(@class, 'navigation-link')]/a")

        elements[1].click()

        self.driver.implicitly_wait(1)  # seconds

        self.driver.find_element_by_id(
            'id_email').send_keys('conor@tests1234.com')
        self.driver.find_element_by_id(
            'id_username').send_keys('conor')
        self.driver.find_element_by_id(
            'id_password1').send_keys('example1aslkfjlksjflaf')
        self.driver.find_element_by_id(
            'id_password2').send_keys('example1aslkfjlksjflaf')
        self.driver.find_element_by_id(
            'id_register_button').click()
        self.driver.implicitly_wait(0)  # seconds

        elements_count = self.driver.find_elements_by_xpath("//*[contains(text(), 'A user with that username already exists')]")

        self.assertEqual(len(elements_count), 1)

    def test_register_password_not_match_form(self):

        self.driver.get("http://localhost:8000")
        self.driver.implicitly_wait(0)  # seconds

        elements = self.driver.find_elements_by_xpath(
            "//li[contains(@class, 'navigation-link')]/a")

        elements[1].click()

        self.driver.implicitly_wait(1)  # seconds

        self.driver.find_element_by_id(
            'id_email').send_keys('conor@tests1234.com')
        self.driver.find_element_by_id(
            'id_username').send_keys('conor')
        self.driver.find_element_by_id(
            'id_password1').send_keys('example1aslkfjlksjflaf')
        self.driver.find_element_by_id(
            'id_password2').send_keys('example1aslkfjlkDDDsjflaf')
        self.driver.find_element_by_id(
            'id_register_button').click()
        self.driver.implicitly_wait(0)  # seconds

        elements_count = self.driver.find_elements_by_xpath("//*[contains(text(), 'Passwords must match')]")

        self.assertEqual(len(elements_count), 1)

    def test_register_form(self):

        self.driver.get("http://localhost:8000")
        self.driver.implicitly_wait(0)  # seconds

        elements = self.driver.find_elements_by_xpath(
            "//li[contains(@class, 'navigation-link')]/a")
        elements[1].click()

        self.assertEqual(
            self.driver.current_url,
            'http://localhost:8000/accounts/register/')
        self.driver.implicitly_wait(0)  # seconds

        self.driver.find_element_by_id(
            'id_username').send_keys('eddie')
        self.driver.find_element_by_id(
            'id_email').send_keys('eddie@irvine.com')
        self.driver.find_element_by_id(
            'id_password1').send_keys('example2')
        self.driver.find_element_by_id(
            'id_password2').send_keys('example2')
        self.driver.find_element_by_id(
            'id_register_button').click()
        self.driver.implicitly_wait(0)  # seconds

        elements_count = self.driver.find_elements_by_xpath("//*[contains(text(), 'You have successfully registered')]")

    def test_login_form(self):

        self.driver.get("http://localhost:8000")
        self.driver.implicitly_wait(0)  # seconds

        elements = self.driver.find_elements_by_xpath(
            "//li[contains(@class, 'navigation-link')]/a")

        elements[0].click()

        self.assertEqual(
            self.driver.current_url, 'http://localhost:8000/accounts/login/')
        self.driver.implicitly_wait(0)  # seconds

        self.driver.find_element_by_id(
            'id_username').send_keys('conor@conor.com')
        self.driver.find_element_by_id(
            'id_password').send_keys('example1')
        self.driver.find_element_by_id(
            'id_login_button').click()

        self.driver.implicitly_wait(0)  # seconds
        self.driver.get("http://localhost:8000")
        self.driver.implicitly_wait(0)  # seconds

        elements = self.driver.find_elements_by_xpath(
            "//li[contains(@class, 'navigation-link')]/a")

        li_text = []

        for element in elements:
            li_text.append(element.text)

        test_list = ['Profile', 'Logout']

        self.assertListEqual(test_list, li_text)

    def test_logout_form(self):

        self.driver.get("http://localhost:8000")
        self.driver.implicitly_wait(0)  # seconds

        elements = self.driver.find_elements_by_xpath(
            "//li[contains(@class, 'navigation-link')]/a")

        elements[1].click()

        elements = self.driver.find_elements_by_xpath(
            "//li[contains(@class, 'navigation-link')]/a")

        li_text = []

        for element in elements:
            li_text.append(element.text)

        test_list = ['Login', 'Register']

        self.assertListEqual(test_list, li_text)


if __name__ == '__main__':
    unittest.main(warnings='ignore')
