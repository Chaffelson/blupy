from __future__ import absolute_import

# http://celery.readthedocs.org/en/latest/getting-started/first-steps-with-celery.html#first-steps

import os
import logging

logger = logging.getLogger(__name__)

from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blupy.settings')

from django.conf import settings

app = Celery('blupy')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS, related_name='tasks')


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
