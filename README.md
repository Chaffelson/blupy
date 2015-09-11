# Overview
I spent some time pulling together information from various sources to deploy Django + Celery to Bluemix as I wanted to combine IBM Watson and Python NLP tools.

I also thought it would be helpful for the community to put all of it together in one place for reuse, so here it is.

This repo contains a functional example application with all necessary configuration files to deploy directly to Bluemix with a little bit of setup.
It demonstrates using Celery workers to add two numbers initiated by a Django admin interface, passing messages via RabbitMQ, and logging activity to an external log aggregator.
It makes extensive use of various PaaS offerings to demonstrate the possibilities.

Additional conveniences have been included to resolve several complexities when deploying Python apps to Bluemix.

## Batteries included

- Simple Django 1.8 application
- Celery 3.1 worker for async tasks 
- RabbitMQ by CloudAMQP for MQ-as-a-service
- Postgres by Compose.io for Database-as-a-service
- Loggly for Logs-as-a-service
- A config resolver for handling environment variables and secret information on PaaS
- Ability to run the same codebase locally or on Bluemix as desired
- Whitenoise to resolve complexities serving Django static files on PaaS
- Finalware to resolve Django admin and sites setup complexities on PaaS


## Assumptions
I assume that you are already familiar with Python programming and the creation and management of your own environment.

As this is intended as an example for how you would put a common Django application framework into Bluemix, familiarity with Bluemix would be very helpful.

If you are unfamiliar with Bluemix you may wish to follow the basic tutorial offered when downloading the Cloud Foundry CLI in the links section.

## Contact
@Chaffleson or daniel@goodforgoodbusiness.com

## Handy dandy links
### Documentation for services
- https://docs.djangoproject.com/en/1.8/
- http://celery.readthedocs.org/en/latest/django/first-steps-with-django.html
- https://whitenoise.readthedocs.org/en/latest/
- https://github.com/un33k/django-finalware

### Service signup pages
- https://console.ng.bluemix.net/?direct=classic
- https://app.compose.io/signup/svelte
- https://www.loggly.com/signup/

### Useful downloads
- https://www.ng.bluemix.net/docs/starters/install_cli.html
- https://www.python.org/downloads/


# Instructions

## Environment Setup

- You will need the Cloud Foundry CLI available at https://www.ng.bluemix.net/docs/starters/install_cli.html
- You will need to clone this repo somewhere on your machine  https://github.com/Chaffleson/blupy.git
- if you want to use this as a basis for your own development I suggest you fork it
- Download or create fresh virtualenv for Python 2.7.10
- Install requirements.txt

## Services setup
You will have to create the services you wish to use, ready for your app instances to link to.
You may obviously configure other services if you wish, I have used the following for the example:

- You will need a Bluemix account with about 256Mb of free hosting memory
    - You can sign up for a free trial at https://console.ng.bluemix.net
- You will then need:
    - A Postgres Database instance
    - A RabbitMQ service
    - A loggly account
    - The services I have used are detailed below
- Compose.io are a IBM affiliate offering Postgres-as-a-service
    - Create a new database under your postgres Compose.io account named 'example01'
    - Register your compose.io account Postgres instance as a service in your Bluemix console
    - Note that the user/pword/url are listed in the Compose.io console for the db, not the account you log in with
    - Note the name that it is registered as in your dashboard, it'll be something like 'PostgreSQL by Compose-bx'
- CloudAMPQ are an IBM affiliate offering RabbitMQ-as-a-service
    - You can register for the service via the Bluemix portal
    - Create a new free-tier 'little lemur' instance
    - Note the name that it is registered as in your dashboard, it'll be something like 'CloudAMQP-sa'
- Loggly are an independent service who offer easily integrated Python log aggregation
    - You can register for the service at loggly.com
    - Once you have your free account, you can get your token for the config file in Source Setup > Customer Tokens
    - Note down the token

## Deployment Instructions

- Follow the environment setup to prepare a Python environment and example code
- Follow the Services Setup instructions to prepare your App Services on Bluemix
- Modify the services statement in manifest.yml to be the name of your services noted down earlier
- Choose a unique URL for your deployment of the example application
    - manifest.yaml; change 'blupy' to your URL in both lines
    - settings_global.py: change 'blupy.mybluemix.net' to your URL
    - Your URL must be unique on the Bluemix platform or deployment will fail
- Uncomment the 'settings_local' line in the .gitignore before you modify your secret information and commit your fork!
- Modify the secret information in settings_local.py to set your own password, loggly token, and Django secret
- You may also wish to review and modify /blupy/settings.py for Django to set your own superusername etc.
- Open up your command prompt in the project root. i.e. ./blupy
- run 'cf login' and follow the prompts for your Bluemix console login
- run 'cf push' and watch the results
    - you can run 'cf logs <yourappname> --recent' to see the dump output
    - you can run 'cf logs <yourappname>' to stream new log entries to your console
    - you can view the application logging output in your loggly console
    - you can go to your Bluemix dashboard to review application status
- you can go to your url on mybluemix.net to login and test your application
    - Go to the url for your application after successful deployment
    - login with the username and password you set in the config
    - go to the 'Adders' admin panel
    - Click 'Add Adder +' in the top right corner
    - Submit a pair of x and y variables leaving Result blank, hit Save.
    - The Celery workers will complete the result and the answer will display on the Adder admin page.
    
## Additional Deployment Options

Once you have configured your services in the Bluemix console and attached them to at least one deployed app, you can then
make a copy of the 'Environment Variables' in the deployed app's console and put that into the settings_local.py file.
This will then allow you to run the Django code locally against the configured remote services for swifter development.

You can also obviously substitute other services into this configuration dictionary, I personally run a local postgres
and rabbitmq service for responsiveness. The confresolver will identify whether you are running on Bluemix or locally and select the config appropriately.