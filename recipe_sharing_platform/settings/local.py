from .base import *

#local-scidfic settings
DEBUG=True
ALLOWED_HOSTS=['127.0.0.1', 'localhost']

#SQL LITE as local DB for dev/test
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlitte3'
    }
}

#Media file
MEDIA_URL='/media/'
MEDIA_ROOT=BASE_DIR / 'media'