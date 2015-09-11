# UPDATE THIS SECRET INFORMATION ! #
# UNCOMMENT THIS FILE IN .gitignore BEFORE YOU COMMIT! #

# SuperUser Default Password
SUPER_USER_PASSWORD = 'CHANGEME'

# Log into your Loggly account, visit: https://<Username>.loggly.com/tokens and copy the token here
LOGGLY_TOKEN = 'CHANGEME'

# Generate a very secure Django Secret to replace this one
DJANGO_SECRET = 'CHANGEME'


# OPTIONAL #

# Replace the following with a copy of your environment variables if you wish to run the code locally
# THe variables will only be available after you first deploy an app to Bluemix, whether the deployment succeeds or not.

LOCALDEV_VCAP = {
   "cloudamqp": [
      {
         "name": "CloudAMQP-sa",
         "label": "cloudamqp",
         "plan": "lemur",
         "credentials": {
            "uri": "amqp://CHANGEME:CHANGEME/CHANGEME",
            "http_api_uri": "https://CHANGEME:CHANGEME/api/"
         }
      }
   ],
   "user-provided": [
      {
         "name": "PostgreSQL by Compose-lj",
         "label": "user-provided",
         "credentials": {
            "username": "CHANGEME",
            "password": "CHANGEME",
            "public_hostname": "localhost:5432"
         }
      }
   ]
}
