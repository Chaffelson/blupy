"""
Settings resolver file - DO NOT PUT SETTINGS IN THIS FILE

Default/Global settings go in <project>.settings_global, and are in source control

Local/Dev settings go in <project>.settings_local, and are NOT in source control.
You should therefore be careful in adding them to .gitignore BEFORE committing.
This is useful for unittest params and authentication or other secret information
"""

from os import environ, getcwd
from platform import node
import logging
import logging.config
from json import loads
from re import findall
# loggly.handlers is a necessary dependency for the log aggregator, even though it is not called
import loggly.handlers


from settings_global import *

try:
    from settings_local import *
except ImportError:
    pass

# A unique identifier for this Python instance, handy for log segregation
INSTANCE = unicode(id(__name__))

# Attempt to determine whether we are running in a LocalDev or Bluemix environment
if u'VCAP_SERVICES' in environ:
    ENVIRONMENT = u'Bluemix'
else:
    ENVIRONMENT = u'LocalDev'

# Logging Setup
# We need to replace the two placeholders for our Loggly Token and Instance ID
LOGGING[u'handlers'][u'loggly'][u'url'] = LOGGING[u'handlers'][u'loggly'][u'url'].replace(
    u'LOGGLY_TOKEN', LOGGLY_TOKEN)
LOGGING[u'formatters'][u'basic'][u'format'] = LOGGING[u'formatters'][u'basic'][u'format'].replace(
    u'INSTANCE', INSTANCE)

# Then we run our logging init and issue our opening message
logging.config.dictConfig(LOGGING)
logger = logging.getLogger(__name__)
logger.warning(u"Conf module imported to new [{0}] instance [{1}] on host [{2}] in workingdir [{3}]".format(
    ENVIRONMENT,
    INSTANCE,
    node(),
    getcwd()
))

# Deal with the Bluemix environment variables which inform what services are available
# Based on http://blog.4loeser.net/2014/08/using-db2-with-python-on-cloud-foundry.html
logger.debug(u'Attempting to load Environment Variables')
if ENVIRONMENT == u'Bluemix':
    SERVICE_INFO = loads(environ[u'VCAP_SERVICES'])
elif ENVIRONMENT == u'LocalDev':
    SERVICE_INFO = LOCALDEV_VCAP
else:
    SERVICE_INFO = []

# Convert Service Info list into a consistent dictionary
BOUND_SERVICES = {}
if SERVICE_INFO is not []:
    logger.debug(u'Environment Variables loaded from {0} data'.format(ENVIRONMENT))
    for outer in SERVICE_INFO:
        for inner in SERVICE_INFO[outer]:
            key = findall(r"[\w]+", inner['name'])[0]
            BOUND_SERVICES[key] = inner
else:
    logger.critical(u'Environment Variables unavailable, terminating.')
    exit()


