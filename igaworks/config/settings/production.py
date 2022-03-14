import os
from turtle import dot

from dotenv import load_dotenv
import pymysql

from .base import *

load_dotenv(dotenv_path=os.path.join(BASE_DIR, 'settings/.env.production'), verbose=True)

DEBUG = False
ALLOWED_HOSTS = ["*"]

SECRET_KEY = os.environ.get('SECRET_KEY')

# WSGI application
WSGI_APPLICATION = 'config.wsgi.production.application'


pymysql.install_as_MySQLdb()
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('DB_NAME', ''),
        'USER': os.environ.get('DB_USER', ''),
        'PASSWORD': os.environ.get('DB_PASSWORD', ''),
        'HOST': os.environ.get('DB_HOST', '127.0.0.1'),
        'PORT': '3306'
    }
}
