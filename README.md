# verbose-pancake

The purpose of this application is provide an easy way to track bugs and features for payment.

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
  * ```python3 -m unittest tests/<replace with files>```

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

### Get Category (Show all fixture categories)

* As a user I want to see............

  * Acceptance criteria:
    * 3...................

## Manual Testing

### Remember Me

* Open 'http:://localhost:5000/register.html' template, enter username, email, password and repeat password fields.  Go to 'http:://localhost:5000/logout' url and then go to 'http:://localhost:5000/login.html' and enter the same email and password with the 'remember_me' checkbox ticked.  Close the browser tab and then reopen and go to 'http:://localhost:5000/get_recipes', you should be shown the Recipes list page 'http:://localhost:5000/get_recipes.html' and not the 'http:://localhost:5000/login' page.

### Small Screen / Mobile menu

* Reduce the size of the webpage on any page and the menu bar links on the right should disappear and the 'hamburger' on the left will appear, click on the 'hamburger' and the slideout mobile menu with all links should appear, click on a menu link and the required page will load and the side menu will close.

## Known Issues

* ......................
[![Build Status](https://www.travis-ci.org/ramblingbarney/furry-waffle.svg?branch=master)](https://www.travis-ci.org/ramblingbarney/furry-waffle)
