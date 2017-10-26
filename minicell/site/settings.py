"""
Django settings
:Author: Jonathan Karr <karr@mssm.edu>
:Date: 2017-10-25
:Copyright: 2017, Karr Lab
:License: MIT
"""

import os

BASE_DOMAIN = 'minicell.org'
BASE_URL = 'http://' + BASE_DOMAIN
ROOT_DOMAIN = 'www.' + BASE_DOMAIN
ROOT_URL = BASE_URL

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '9r!@p)aofg)n%7tlfmre=d%6f#g6&wma%#w9rq+ky+v*9e$y@0'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
    BASE_DOMAIN, 
    'www.' + BASE_DOMAIN, 
]


# Application definition

INSTALLED_APPS = [
    #'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    #'django.contrib.sessions',
    #'django.contrib.messages',
    #'django.contrib.staticfiles',
    'minicell.core',
]

MIDDLEWARE = [
    #'django.middleware.security.SecurityMiddleware',
    #'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    #'django.contrib.auth.middleware.AuthenticationMiddleware',
    #'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'minicell.site.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'core', 'templates'),
        ],
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

WSGI_APPLICATION = 'minicell.site.wsgi.application'


# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'minicell',                    # Or path to database file if using sqlite3.
        'USER': 'minicell',                    # Not used with sqlite3.
        'PASSWORD': 'cgGBSXk7LuL6Zsh8eNgNvsTe',# Not used with sqlite3.
        'HOST': 'mysql.minicell.org',          # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                            # Set to empty string for default. Not used with sqlite3.
    }
}


# Password validation

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'

''' Logging '''

LOG_DIR = os.path.join(BASE_DIR, 'log')
LOG_FILE = os.path.join(LOG_DIR, 'error.log')

if not os.path.isdir(LOG_DIR):
    os.mkdir(LOG_DIR)
if not os.path.isfile(LOG_FILE):
    with open(LOG_FILE, 'w'):
        os.utime(LOG_FILE, None)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
    },
    'handlers': {
        'file': {
            'formatter': 'verbose',
            'level': 'WARNING',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': LOG_FILE,
            'maxBytes': 1024*1024*5, # 5 MB
            'backupCount': 5,
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

#login URL
LOGIN_URL = ROOT_URL + '/login'
LOGIN_REDIRECT_URL = ROOT_URL + '/'