from .base import *


DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': env('POSTGRES_DB'),
        'USER': env('POSTGRES_USER'),
        'PASSWORD': env('POSTGRES_PASS'),
        'HOST': env('PG_HOST'),
        'PORT': env('PG_PORT'),
    }
}