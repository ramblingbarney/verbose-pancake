from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.contrib.sessions.models import Session
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from django.core import management
from django.core.management.commands import loaddata


class SiteLoginLogout(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        management.call_command('flush', verbosity=0, interactive=False)
        management.call_command(
            'loaddata',
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

        self.driver.get("http://localhost:8000")
        self.driver.implicitly_wait(0)  # seconds

        self.driver.find_element_by_xpath(
            "//i[contains(@class, 'fa-sign-in-alt')]").click()

        self.driver.implicitly_wait(0)  # seconds

        self.driver.find_element_by_id(
            'id_username').send_keys('conorXXXXX@conor.com')
        self.driver.find_element_by_id(
            'id_password').send_keys('example1aslkfjlksjflaf')
        self.driver.find_element_by_id(
            'id_login_button').click()
        self.driver.implicitly_wait(0)  # seconds

        elements_count = self.driver.find_elements_by_xpath(
            "//*[contains(text(), 'Your username or password is incorrect')]")

        self.assertEqual(len(elements_count), 1)

    def test_register_duplicate_email_form(self):

        self.driver.get("http://localhost:8000")
        self.driver.implicitly_wait(0)  # seconds

        self.driver.find_element_by_id('desktop-menu').click()

        self.driver.implicitly_wait(0)  # seconds

        self.driver.find_element_by_xpath(
            "//div/a[contains(text(), 'Register')]").click()

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

        elements_count = self.driver.find_elements_by_xpath(
            "//*[contains(text(), 'Email address must be unique')]")

        self.assertEqual(len(elements_count), 1)

    def test_register_duplicate_user_form(self):

        self.driver.get("http://localhost:8000")
        self.driver.implicitly_wait(0)  # seconds

        self.driver.find_element_by_id('desktop-menu').click()

        self.driver.implicitly_wait(0)  # seconds

        self.driver.find_element_by_xpath(
            "//div/a[contains(text(), 'Register')]").click()

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

        elements_count = self.driver.find_elements_by_xpath(
            "//*[contains(text(), 'A user with that username already exists')]")

        self.assertEqual(len(elements_count), 1)

    def test_register_password_not_match_form(self):

        self.driver.get("http://localhost:8000")
        self.driver.implicitly_wait(0)  # seconds

        self.driver.find_element_by_xpath(
            "//i[contains(@class, 'fa-sign-out-alt')]").click()

        self.driver.implicitly_wait(0)  # seconds

        self.driver.find_element_by_id('desktop-menu').click()

        self.driver.implicitly_wait(0)  # seconds

        self.driver.find_element_by_xpath(
            "//div/a[contains(text(), 'Register')]").click()

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

        elements_count = self.driver.find_elements_by_xpath(
            "//*[contains(text(), 'Passwords must match')]")

        self.assertEqual(len(elements_count), 1)

    def test_register_form(self):

        self.driver.get("http://localhost:8000")
        self.driver.implicitly_wait(0)  # seconds

        self.driver.find_element_by_id('desktop-menu').click()

        self.driver.implicitly_wait(0)  # seconds

        self.driver.find_element_by_xpath(
            "//div/a[contains(text(), 'Register')]").click()

        self.driver.implicitly_wait(0)  # seconds

        self.driver.find_element_by_id(
            'id_username').send_keys('eddie1')
        self.driver.find_element_by_id(
            'id_email').send_keys('eddie1@irvine.com')
        self.driver.find_element_by_id(
            'id_password1').send_keys('example21')
        self.driver.find_element_by_id(
            'id_password2').send_keys('example21')
        self.driver.find_element_by_id(
            'id_register_button').click()
        self.driver.implicitly_wait(0)  # seconds

        elements_count = self.driver.find_elements_by_xpath(
            "//*[contains(text(), 'You have successfully registered')]")

        self.assertEqual(len(elements_count), 1)

        elements_count = self.driver.find_elements_by_xpath(
            "//*[contains(text(), 'pages about the site')]")

        self.assertEqual(len(elements_count), 1)

    def test_login_form(self):

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
        self.driver.get("http://localhost:8000")
        self.driver.implicitly_wait(0)  # seconds

        self.driver.find_element_by_id('desktop-menu').click()

        self.driver.implicitly_wait(0)  # seconds

        self.driver.find_element_by_xpath(
            "//div/a[contains(text(), 'Profile')]").click()

        self.assertEqual(1, 1)

    def test_logout_form(self):

        self.driver.get("http://localhost:8000")
        self.driver.implicitly_wait(0)  # seconds

        self.driver.find_element_by_xpath(
            "//i[contains(@class, 'fa-sign-out-alt')]").click()

        self.driver.get("http://localhost:8000")
        self.driver.implicitly_wait(0)  # seconds

        self.driver.find_element_by_id('desktop-menu').click()

        self.driver.find_element_by_xpath(
            "//div/a[contains(text(), 'Register')]").click()

        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main(warnings='ignore')
