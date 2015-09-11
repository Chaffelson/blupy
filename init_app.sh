#!/bin/sh
# From http://blog.banck.net/2014/12/deploying-a-django-application-to-cloud-foundry/#comment-3967
# echo "------ Create database tables ------"
python manage.py migrate

# run app
gunicorn blupy.wsgi --workers=3