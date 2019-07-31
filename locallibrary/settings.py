"""
Django settings for locallibrary project.

Generated by 'django-admin startproject' using Django 2.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# pg 96
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# We do this to avoid hardcoding file paths.
# To fix the path issue, we dynamically set a project root variable intuitively named BASE DIR at the
# top of the base settings module. Since BASE DIR is determined in relation to the location of base.py,
# your project can be run from any location on any development computer or server.

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# used to provide cryptographic signing, and should be set to a unique, unpredictable value.


SECRET_KEY = 'b26n4h!9rx@&i3f127v-h56+ga0j44m%s$ij$e-ribzinq%@+9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# host/domain names that this Django site can serve
ALLOWED_HOSTS = ['0.0.0.0','127.0.0.1']


# Application definition
# all applications that are enabled 
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'catalog',
    'feedback',
]



# Middleware is a framework of hooks into Django’s request/response processing. 
# It’s a light, low-level “plugin” system for globally altering Django’s input or output.
# Each middleware component is responsible for doing some specific function
# e.g AuthenticationMiddleware, that associates users with requests using sessions.

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# A string representing the full Python import path to your 
# root URLconf, for example "mydjangoapps.urls"

ROOT_URLCONF = 'locallibrary.urls'


# A list containing the settings for all template engines to be used with Django. 
# Each item of the list is a dictionary containing the options for an individual engine.

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# The full Python path of the WSGI application object that Django’s built-in servers 
# (e.g. runserver) will use

WSGI_APPLICATION = 'locallibrary.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

# A dictionary containing the settings for all databases to be used with Django.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # The database backend to use
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'), # The name of the database to use.
    }
}
# eg, for postgresql

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'mydatabase',
#         'USER': 'mydatabaseuser',
#         'PASSWORD': 'mypassword', # The password to use when connecting to the database
#         'HOST': '127.0.0.1', # Which host to use when connecting to the database
#         'PORT': '5432', # The port to use when connecting to the database
#     }
# }




# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators


# The list of validators that are used to check the strength of user’s passwords.

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

# A string representing the language code for this installation.
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Nairobi'

# USE_I18N must be active for language_code setting to have any effect.

# It serves two purposes:

# If the locale middleware isn’t in use, it decides which translation is served to all users.
# If the locale middleware is active, it provides a fallback language in case the user’s preferred 
# language can’t be determined or is not supported by the website. It also provides the fallback 
# translation when a translation for a given literal doesn’t exist for the user’s preferred language.

USE_I18N = True # A boolean that specifies whether Django’s translation system should be enabled.

# if USE_L10N is set to True, then the locale-dictated format has 
# higher precedence and will be applied instead.
USE_L10N = True # A boolean that specifies if localized formatting of data will be enabled by default or not.

# Use pytest to run all tests
TEST_RUNNER = 'django_pytest.test_runner.TestRunner'


# When USE_TZ is True and the database doesn’t support time zones (e.g. SQLite, MySQL, Oracle), Django reads and writes datetimes in local time according to this option if it is set and in UTC if it isn’t.

# When USE_TZ is True and the database supports time zones (e.g. PostgreSQL), it is an error to set this option.

# When USE_TZ is False, it is an error to set this option.

USE_TZ = True # A boolean that specifies if datetimes will be timezone-aware by default or not.


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Redirect to home URL after login (Default redirects to /accounts/profile/)
# The URL or named URL pattern where requests are redirected after login
LOGIN_REDIRECT_URL = '/'

# The backend to use for sending emails
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'




# CELERY
BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Africa/Nairobi'

# Emails
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025
DEFAULT_FROM_EMAIL = 'locallibrary <locallibrary@example.com>'

REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle'
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '100/day',
        'user': '1000/day'
    }
}