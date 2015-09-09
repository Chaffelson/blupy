# Replace the following sections as instructed to allow local development to function as if running on Bluemix


# Log into your Loggly account, visit: https://<Username>.loggly.com/tokens and copy the token here
LOGGLY_TOKEN = 'SomethingSecret'

# Generate a very secure Django Secret to replace this one
DJANGO_SECRET = 'NotAVeryGoodSecretAtAll'

# Replace the following with a copy of your environment variables.
# THe variables will only be available after you first deploy an app to Bluemix
LOCALDEV_VCAP = {
   "cloudamqp": [
      {
         "name": "CloudAMQP-sa",
         "label": "cloudamqp",
         "plan": "lemur",
         "credentials": {
            "uri": "SomethingSecret",
            "http_api_uri": "SomethingSecret"
         }
      }
   ],
   "user-provided": [
      {
         "name": "PostgreSQL by Compose-lj",
         "label": "user-provided",
         "credentials": {
            "username": "SomethingSecret",
            "password": "SomethingSecret!",
            "public_hostname": "SomethingSecret"
         }
      }
   ]
}