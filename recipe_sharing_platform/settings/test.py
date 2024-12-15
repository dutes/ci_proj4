from .base import *

#test-specific settings
DEBUG=False
ALLOWED_HOSTS=['127.0.0.1']

#Test postgres db
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME', 'recipe_sharing_db'),
        'USER': os.getenv('DB_USER', 'recipe_user'),
        'PASSWORD': os.getenv('DB_PASSWORD', 'password'),
        'HOST': os.getenv('DB_HOST', 'localhost'),
        'PORT': os.getenv('DB_PORT', '5432'),
    }
}

