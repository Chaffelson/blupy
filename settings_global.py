# Placeholders for Settings_Global parameters
LOGGLY_TOKEN = ''
DJANGO_SECRET = ''
LOCALDEV_VCAP = ''

# Logging Config
# Note that all logging is set to debug by default, you may wish to change this

LOGGING = {

    u'version': 1,
    u'disable_existing_loggers': True,
    u'handlers': {
        u'loggly': {
            u'class': u'loggly.handlers.HTTPSHandler',
            u'formatter': u'basic',
            u'level': u'DEBUG',
            u'url': u'https://logs-01.loggly.com/inputs/LOGGLY_TOKEN'
        },
        u'console': {
            u'class': u'logging.StreamHandler',
            u'level': u'DEBUG',
            u'formatter': u'basic',
            u'stream': u'ext://sys.stdout',
        }
    },
    u'formatters': {
        u'basic': {
            u'format': u'INSTANCE|%(filename)15s:%(lineno)03d|%(name)s:%(levelname)-8s|%(message)s'
        }
    },
    u'loggers': {
        # Default Root logger
        u'root': {
            u'level': u'DEBUG',
            u'propagate': True,
            u'handlers': [u'loggly']
        },
        # Default Modele loggers
        u'django': {
            u'level': u'DEBUG',
            u'propagate': True,
            u'handlers': [u'loggly']
        },
        u'celery': {
            u'level': u'INFO',
            u'propagate': True,
            u'handlers': [u'loggly']
        },
        # Logger for our custom Config resolver
        u'confresolver': {
            u'level': u'DEBUG',
            u'propagate': True,
            u'handlers': [u'loggly']
        },
        # Here is our Celery App Task Logger
        u'example.tasks': {
            u'level': u'DEBUG',
            u'propagate': True,
            u'handlers': [u'loggly']
        }
    }
}
