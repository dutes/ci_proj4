"""
Django settings for recipe_sharing_platform project.

Generated by 'django-admin startproject' using Django 4.0.
"""

from pathlib import Path
import os
import base64
from decouple import config
from google.oauth2 import service_account
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY', default='your-default-secret-key')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

# Allowed hosts
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='127.0.0.1').split(',')

# Application definition
INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'recipe_share_app',
    'storages',  # For Google Cloud Storage
]

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',  # For Heroku deployment
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'recipe_sharing_platform.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'recipe_sharing_platform.wsgi.application'

# Database configuration
DATABASES = {
    'default': dj_database_url.config(default=os.environ.get('DATABASE_URL'))
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

# login logout urls
LOGIN_URL = 'login' # redirects to the modal login view
LOGIN_REDIRECT_URL = 'index' #redirects index view post login
LOGOUT_REDIRECT_URL = 'index' #redirect after logout

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Media files
if DEBUG:
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
else:
    MEDIA_URL = f'https://storage.googleapis.com/{config("GS_BUCKET_NAME")}/'

# Google Cloud Storage Configuration
GS_BUCKET_NAME = config('GS_BUCKET_NAME', default='my-recipe-images')
GOOGLE_APPLICATION_CREDENTIALS_BASE64 = os.getenv('GOOGLE_APPLICATION_CREDENTIALS_BASE64')

if GOOGLE_APPLICATION_CREDENTIALS_BASE64:
    google_creds_path = os.path.join(BASE_DIR, 'google-credentials.json')
    with open(google_creds_path, 'wb') as creds_file:
        creds_file.write(base64.b64decode(GOOGLE_APPLICATION_CREDENTIALS_BASE64))
    print(f'Google Cloud Storage credentials saved to {google_creds_path}')
    GS_CREDENTIALS = service_account.Credentials.from_service_account_file(google_creds_path)
else:
    raise Exception("GOOGLE_APPLICATION_CREDENTIALS_BASE64 not found in environment variables.")

DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'

# Django Heroku settings
import django_heroku
django_heroku.settings(locals())

#session settings
SESSION_ENGINE='django.contrib.sessions.backends.db'
SESSION_COOKIE_HTTPPONLY = True
SESSION_COOKIE_SECURE=False
CSRF_COOKIE_SCENE=False