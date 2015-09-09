# Things we cover

- Simple Django application using:
    - Celery workers for async tasks 
    - RabbitMQ for message passing
    - Postgres for Database
    - Loggly for Log aggregation
    - A handy config parser for handling environment variables


# Assumptions

I assume that you are already familiar with Python programming and the creation and management of your own environment.
This is intended as a guide for how you would put a common Django application framework into Bluemix.
I also assume that you already have a Bluemix account and understand how to sign up for services.


# Services setup
You will have to create the services you wish to use, ready for your app instances to link to

- Compose.io are a IBM affiliate offering Postgres-as-a-service
    - Create a new database under your postgres Compose.io account named 'example'
    - Register your compose.io account Postgres instance as a service in your Bluemix console
- CloudAMPQ are an IBM affiliate offering RabbitMQ-as-a-service
    - You can register for the service via the Bluemix portal
    - Create a new free-tier 'little lemur' instance
- Loggly are an independent service who offer easily integrated Python log aggregation
    - You can register for the service at loggly.com
    - Once you have your free account, you can get your token for the config file in Source Setup > Customer Tokens

# Deployment Instructions

- Follow the Services Setup instructions to prepare your App Services on Bluemix
- Uncomment the 'settings_local' line in the .gitignore before you modify your secret information and commit your fork!

# Local Install Instructions

- Download or create fresh virtualenv for Python 2.7.10
- Install requirements.txt
