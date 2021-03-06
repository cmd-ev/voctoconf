import os
import environ

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)
# reading .env file
#environ.Env.read_env()

# False if not in os.environ
DEBUG = env('DEBUG')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# defaults
SECRET_KEY = env('SECRET_KEY')

# conference name
CONFERENCE_NAME = env('CONFERENCE_NAME', default='TEST CONFERENCE')
THEME = env('THEME', default="piandmore")

# this setting is used to disable public pages
PAGE_LIVE = env('PAGE_LIVE', default=DEBUG)
CHAT_ENABLED = env('CHAT_ENABLED', default=False)
SIGNUP_ENABLED = env('SIGNUP_ENABLED', default=False)

# To properly embed BBB in iframes, BBB must explicitly use SameSite=None for its session cookies. Otherwise, modern browsers cannot access BBB anymore. Workaround: we do not use frames and redirect users directly to BBB.
BBB_NOFRAME = True

BASE_URL = env('BASE_URL', default="http://localhost:8000/")
ALLOWED_HOSTS = ["*"]

BBB_SECRETS_DIR = os.path.join(BASE_DIR, "_bbb_secrets")
STATIC_ROOT = os.path.join(BASE_DIR, "_static")
MEDIA_ROOT = os.path.join(BASE_DIR, "_media")

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    os.path.join(BASE_DIR, "themes", THEME, "static"),
]
STATICFILES_FINDERS = [
    'compressor.finders.CompressorFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

MEDIA_URL = '/media/'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, '_db.sqlite3'),
    }
}


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': '[DJANGO] %(levelname)s %(asctime)s %(module)s '
            '%(name)s.%(funcName)s:%(lineno)s: %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'default',
        }
    },
    'loggers': {
        '*': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        }
    },
}

# alternate logging - this yields debug output
#LOGGING = {
#    'version': 1,
#    'disable_existing_loggers': False,
#    'handlers': {
#        'console': {
#            'class': 'logging.StreamHandler',
#        },
#    },
#    'loggers': {
#        'django': {
#            'handlers': ['console'],
#            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
#        },
#    },
#}

# Application definition
INSTALLED_APPS = [
    'macros',
    'channels',
    'chat',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'landingpage',
    'partners',
    'bbb',
    'eventpage',
    'helpers',
    'authstuff',
    'staticpages',
    'compressor',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'authstuff.middleware.NameMiddleware',
]

ROOT_URLCONF = 'voctoconf.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            os.path.join(BASE_DIR, 'themes', THEME, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.i18n',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'voctoconf.context_processors.add_conference_metadata',
            ],
        },
    },
]

WSGI_APPLICATION = 'voctoconf.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_USER_MODEL = 'authstuff.User'
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en'
LANGUAGES = (
    ('en', 'English'),
    ('de', 'Deutsch'),
)

TIME_ZONE = 'Europe/Berlin'

USE_I18N = True

USE_L10N = True

USE_TZ = True

ASGI_APPLICATION = 'voctoconf.routing.application'
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('redis', 6379)],
        },
    },
}

LIBSASS_PRECISION = 8

LIBSASS_OUTPUT_STYLE = 'compressed'

COMPRESS_PRECOMPILERS = (
    ('text/x-scss', 'django_libsass.SassCompiler'),
)

COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
]

COMPRESS_CSS_HASHING_METHOD = 'mtime'


#try:
#    from .local_settings import *
#except:
#    print("#############")
#    print("## WARNING ##")
#    print("#############")
#    print("")
#    print("NO LOCAL CONFIGURATION FOUND")
#    print("USING DEV DEFAULTS")
#    print("DONT RUN THIS ON THE INTERWEBZ")
#    print("")
#
#if not DEBUG and SECRET_KEY == DEFAULT_SECRET_KEY:
#    print("LOL NOPE")
#    sys.exit(1)
#
