from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

#para ejecutar esta base de datos con el usuario que habia creado tuve que tambien darles permisos publicos 
#GRANT ALL PRIVILEGES ON SCHEMA public TO tu_usuario;
# para poder hacer el manage.py migrate de forma correcta
"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dbempleado',
        'USER': 'felizola',
        'PASSWORD': 'Romulo23!',
        'HOST': 'localhost',
        'PORT': '5432',

    }
}
"""

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

STATICFILES_DIRS = [BASE_DIR / 'static']

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'

