# verbose-pancake

The purpose of this application is provide an easy way to track bugs/features for payment and to collaborate with fellow team members in real time with a message history.

## Prerequisites

* [Python3](https://www.python.org/)

## Wireframes


## Installation

* ```pip3 install -r /path/to/requirements.txt```
* ```export SECRET_KEY=<complete key>``` SECRET_KEY environment variable

### Running Tests

  * ```python3 manage.py test```

## Deployment

The 'development' and 'testing' of the app have been done on the 'master' branch.  'Coverage' has been calculated on the 'master' branch.

The deployed version (master_heroku) on heroku has the following differences from the 'master' branch

* No testing profile in the config.py file and file uses environment variables instead of hardcoded values.  The 'master' branch does not contain this file so the example version of the file requires hardcoded values as described in the Installation steps.

* The deployed branch uses these heroku configuration variables
  * CURRENT_HOST (app.py home route replacing https://localhost:5000)
  * FLASK_CONFIG
  * MONGO_DBNAME (config.py)
  * MONGO_URI (config.py)
  * SECRET_KEY (config.py)
  * YOURAPPLICATION_SETTINGS

* The webserver specified on heroku is 'gunicorn'
* DEBUG=False and host/port taken from os.environ environment variables
* Heroku config files are 'runtime.txt', 'Procfile' and 'requirements.txt'

## Acceptance tests

### Register

* As a user I want to be able to enter my username, email, password and password confirmation to register with the site and be shown message 'You have successfully registered'

  * Acceptance criteria:
    * Text box and label for;
      * Username
      * Email
      * Passwords
      * Password Confirmation
      * Register Button

### Register Duplicate Email or Username Form Errors

* As a user I want to be prevented from entering usernames and email addresses that are already registered

  * Acceptance criteria:
    * A warning is displayed alerting the user that the email or username has been registered
    * The user cannot submit the form

### Register Password and Password Confirmation not matching Errors

* As a user I want to be alerted when the password and password confirmation text do not match

  * Acceptance criteria:
    * A warning is displayed alerting the user that the password and password confirmation do not match

### Login Failed

* As a user I want to be alerted when either the username or password result in a failed login attempt

  * Acceptance criteria:
    * A warning is displayed alerting the user that either the password or username is incorrect

### Login Success

* As a user I want to be advised when the login has been successful

  * Acceptance criteria:
    * The home page links change
    * A message is displayed confirming a successful login

### Logout

* As a user I want to be advised when I have logged out

  * Acceptance criteria:
    * The home page links change
    * A message is displayed confirming a successful logout

### All Features & Issues

* As a user I want to be shown all created Features & Issues created ( url route /products)

  * Acceptance criteria:
    * Feature/Issue headline contains;
      * Name
      * Price
      * Total Cumulative Donations
      * Status
    * Feature/Issue body contains;
      * Description & Feature/Issue type
      * User uploaded image with fullsize toggle on click
      * Need (Low, Medium or High)
      * Complexity (Low, Medium or High)
      * Attached document to download
    * Feature/Issue body Cart options;
      * Add a vote Button
      * Add specified quantity to the cart Button
      * Edit Feature/Issue button

### Add new Feature or Issue

* As a logged in user I want to be able to create a Feature or Issue ( url route /products/new)

* Acceptance criteria:
  * A new Feature/Issue contains;
    * Name
    * Price
    * Total Cumulative Donations
    * Status
    * Description & Feature/Issue type
    * User uploaded image with fullsize toggle on click
    * Need (Low, Medium or High)
    * Complexity (Low, Medium or High)
    * Attached document to download
    * Votes with default value of 0


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


## Manual Testing

* View the /products url and add a Feature or Issue to the cart, the number of products shown in the cart at the right of the cart graphic should increase by the quanity added to the cart

### Password Reset
Click on the link 'Forgot My Password' and enter your email address, either look on the terminal running the webserver or the email address supplied and open the link in the browser, enter the new password into the input boxes provided and click 'Reset Password'.  Return to the login page and login using the new password.

### Small Screen / Mobile menu

* .....

## Known Issues

[![Build Status](https://www.travis-ci.org/ramblingbarney/verbose-pancake.svg?branch=master)](https://www.travis-ci.org/ramblingbarney/verbose-pancake)
[![codecov.io](https://codecov.io/github/ramblingbarney/verbose-pancake/coverage.svg?branch=master)](https://codecov.io/github/ramblingbarney/verbose-pancake)
