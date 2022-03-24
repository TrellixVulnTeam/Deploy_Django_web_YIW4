"""
*배포환경만 처리합니다.
"""
import os
from .base import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# 암호화 완료
# SECRET_KEY =  os.environ.get('SECRETE_KEY')
SECRET_KEY = os.environ.get('SECRETE_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
DEBUG = False

ALLOWED_HOSTS = ['*']

# 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django',
        'USER': 'django',
        'PASSWORD': 'password1234',
        # Docker Container Name
        'HOST': 'mariadb',
        'PORT': '3306',
    }
}
