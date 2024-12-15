from .base import *
import dj_database_url
import django_heroku

#prod spec settings
DEBUG=False
ALLOWED_HOSTS=['recipe-sharing-app-9034a749d6a6.herokuapp.com']

DATABASES={
    'default': dj_database_url.config(conn_max_age=800)
}

#static file & whitenoise 
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

#heroku config
django_heroku.settings(locals())

#security 
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

