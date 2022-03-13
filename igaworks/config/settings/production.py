import os
from turtle import dot

from dotenv import load_dotenv

from .base import *

load_dotenv(dotenv_path=os.path.join(BASE_DIR, 'settings/.env.production'), verbose=True)

DEBUG = False
ALLOWED_HOSTS = ["*"]

SECRET_KEY = os.getenv('SECRET_KEY')

# WSGI application
WSGI_APPLICATION = 'config.wsgi.development.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
