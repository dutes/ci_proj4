import os

#set default settings based on the ENV
DJANGO_ENV = os.getenv('DJANGO_ENV', 'local')

if DJANGO_ENV == 'production':
    from .production import *
elif DJANGO_ENV == 'test':
    from .test import *
else:
    from .local import *

