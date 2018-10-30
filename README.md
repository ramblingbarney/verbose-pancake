# verbose-pancake

The purpose of this application is provide an easy way to track bugs/features for payment and to collaborate with fellow team members in real time with a message history.

## Prerequisites

* [Python3](https://www.python.org/)

## Wireframes


## Installation

* ```pip3 install -r /path/to/requirements.txt```
* ```npm install --prefix ./static/```
* ```export SECRET_KEY=<complete key>``` SECRET_KEY environment variable

### Running Tests

* Download the latest chromedriver binary: https://sites.google.com/a/chromium.org/chromedriver/downloads, for linux ensure the binary is in your path or for windows provide a full path 'c:\< >.exe' on line 21 of 'test_front_end.py'.  

* Run the following commands
  * ```chromedriver --port=9515```
  * ```python3 manage.py test```

## Test Coverage

Module 	  statements 	missing 	excluded 	coverage

See htmlcov/index.html for full results

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

## Manual Testing

### Password Reset
Click on the link 'Forgot My Password' and enter your email address, either look on the terminal running the webserver or the email address supplied and open the link in the browser, enter the new password into the input boxes provided and click 'Reset Password'.  Return to the login page and login using the new password.

### Small Screen / Mobile menu

*

## Known Issues

* .....................

[![Build Status](https://www.travis-ci.org/ramblingbarney/verbose-pancake.svg?branch=master)](https://www.travis-ci.org/ramblingbarney/verbose-pancake)
