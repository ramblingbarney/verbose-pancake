# verbose-pancake

The purpose of this application is provide an easy way to track bugs/features for payment and to collaborate with fellow team members in real time with a message history.

## Prerequisites

* [Python3](https://www.python.org/)
* [Chromedriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) available in the 'user' path executing tests

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

### Add new Feature or Issue Form Errors

* As a logged in user I want to be able to create a Feature or Issue (url route /products/new) and be prevented from using a 'Name' that exists in the database, upload an image file that is not an image or uploading a document that is too large or not an accepted file type.

* Acceptance criteria:
  * name - Name must be unique
  * image - Upload a valid image. The file you uploaded was either not an image or a corrupted image.
  * product_document - Please keep filesize under 5.0MB. Current filesize N MB

### Add new Feature without Image or Document

* As a logged in user I want to be able to create a Feature (url route /products/new) without an 'Image' file or 'Product Document' file

* Acceptance criteria:
  * name - Name must be unique
  * image - A placeholder image will be shown instead of the Upload image
  * Document - No file will be shown

### Edit Feature Name

* As a logged in user I want to be able to edit the name of a feature and it be reflected on the name of the same feature on the all features and issues page.

* Acceptance criteria:
  * Name will show the amended feature name
  * Image will be unchanged and no error message will be shown
  * Document Image will be unchanged and no error message will be shown

### Edit Feature (save without any changes)

* As a logged in user I want to be able to edit a feature and be prevented from using a 'Name' that exists in the database

* Acceptance criteria:
  * name - Name must be unique

### Add to Cart Feature/Issue Page

* As a logged in user I want to be able to add 2 different products to the cart and the number of products in the cart shown on the navigation page will be 2

* Acceptance criteria:
  * Cart Number = 2

### Add New Feature/Issue Area Page

* As a logged in user I want to be able to add unique Feature/Issue Area options

* Acceptance criteria:
  * Add unique Feature/Issue Area name
  * This additional name is shown in the list of all Feature/Issue Areas

### Add New Feature/Issue Area Page with Error

* As a logged in user I want to be able to add non unique Feature/Issue Area options and be shown an error

* Acceptance criteria:
  * Add non unique Feature/Issue Area name
  * Error message shown 'Name must be unique'

### Edit Feature/Issue Area Page

* As a logged in user I want to be able to edit and save an existing Feature/Issue Area name

* Acceptance criteria:
  * Edit Feature/Issue Area name
  * This edited version is shown in the complete list of all Features/Issues

### Delete Feature/Issue Area Name not used in a Feature/Issue

* As a logged in user I want to be able to delete a Feature/Issue Area Name not used in a Feature/Issue

* Acceptance criteria:
  * Delete Feature/Issue Area name
  * This Feature/Issue Area name is not shown in the complete list of all Features/Issues

### Delete Feature/Issue Area Name used in a Feature/Issue

* As a logged in user I want to be not able to delete a Feature/Issue Area Name used in a Feature/Issue

* Acceptance criteria:
  * Delete Feature/Issue Area name
  * Error message shown '{Feature/Issue Area Name} Cannot be deleted, Please delete Feature/Issue instead'

### Delete Feature/Issue by the Creator/Owner

* As a logged in user and creator/owner of the Feature/Issue I want to be able to delete it

* Acceptance criteria:
  * Delete Feature/Issue name
  * This Feature/Issue Area name is not shown in the complete list of all Features/Issues

### Delete Feature/Issue not by the Creator/Owner

* As a logged in user and not the creator/owner of the Feature/Issue I want to be stopped from deleting it

* Acceptance criteria:
  * Delete Feature/Issue name
  * Error message shown '{Feature/Issue Name}  can only be deleted by the creator'

## Manual Testing

* View the /products url and add a Feature or Issue to the cart, the number of products shown in the cart at the right of the cart graphic should increase by the quantity added to the cart
* View the /products url and click on the '+1 Vote' button for any Feature/Issue, the total vote number should increment by 1 and turn red only allowing one vote per registered user per feature/issue, were the user has voted on the feature/issue before the number of votes will not increment by 1 or turn red

### Password Reset
Click on the link 'Forgot My Password' and enter your email address, either look on the terminal running the webserver or the email address supplied and open the link in the browser, enter the new password into the input boxes provided and click 'Reset Password'.  Return to the login page and login using the new password.

### Small Screen / Mobile menu

* .....

## Known Issues

[![Build Status](https://www.travis-ci.org/ramblingbarney/verbose-pancake.svg?branch=master)](https://www.travis-ci.org/ramblingbarney/verbose-pancake)
[![codecov.io](https://codecov.io/github/ramblingbarney/verbose-pancake/coverage.svg?branch=master)](https://codecov.io/github/ramblingbarney/verbose-pancake)
