from .base import *
import dj_database_url
import django_heroku
import base64
import os
from google.oauth2 import service_account

#prod spec settings
DEBUG=False
ALLOWED_HOSTS=['recipe-sharing-app-9034a749d6a6.herokuapp.com']

DATABASES={
    'default': dj_database_url.config(conn_max_age=800)
}

#static file & whitenoise 
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

#google cloud bucket settings
GS_BUCKET_NAME = os.getenv('GS_BUCKET_NAME')
GOOGLE_APPLICATION_CREDENTIALS_BASE64 = os.getenv('GOOGLE_APPLICATION_CREDENTIALS_BASE64')

if GOOGLE_APPLICATION_CREDENTIALS_BASE64:
    creds_file_path = os.path.join(BASE_DIR, 'google-key.json')
    with open(creds_file_path, 'wb') as creds_file:
        creds_file.write(base64.b64decode(GOOGLE_APPLICATION_CREDENTIALS_BASE64))
    GS_CREDENTIALS = service_account.Credentials.from_service_account_file(creds_file_path)

DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
MEDIA_URL = f'https://storage.googleapis.com/{GS_BUCKET_NAME}/'

#heroku config
django_heroku.settings(locals())

#security 
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

