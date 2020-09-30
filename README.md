# User Activity
# BOOKMARK MANAGER

CONTENTS OF THIS FILE
---------------------

 * Introduction
 * Installation
 * Create Customers
 * API end points
 
 
 INTRODUCTION
------------


The User Activity is a web based application built in Python framework Django. It allows custom commands to populate dummy user data given in JSON file as sample.

 INSTALLATION
------------
The application is easy to install. The user needs to have python version 3 or greater, 
pip package installer. Using a virtual environment is recommended. The application is configured to use the SQLite database which comes with a new Django project setup by default. 

The following steps to setup are.
* Clone this repo 
* Create virtual environment
* Get to the project directory using 'cd user_activity' where 'requirements.txt' exist.
* Install all required packages using  'pip install -r requirements.txt'
* Check the application setup by 'python manage.py check'.
* Makemigrations using 'python manage.py makemigrations userapp'
* Then apply migrations using 'python manage.py migrate'
* Create super user by 'python manage.py createsuperuser', follow the cli for admin credentials.
* Runserver server using 'python manage.py runserver'
* Access the app's admin panel using 127.0.0.1:8000/admin

 CREATE USERS
------------

* To create users, use command 'python manage createusers --path path/to/json/file'.
* One sample json file is provided within the root directory of this project to use it simply fire 'python manage.py createusers --path dummydata.json' without changing the path of this file.


 API endpoints
------------
* This APP is configured to use Django restframe work BasicAuthentication and IsAuthenticated permission required settings.
* Currently there are one endpoints available
  * '/api/users' - Accepts GET request. The endpoint will return all available 
    users with their associated activity periods if exists.