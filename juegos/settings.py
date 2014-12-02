"""
Django settings for juegos project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
RUTA_PROYECTO=os.path.dirname(os.path.realpath(__file__))
#MEDIA_ROOT=os.path.join(RUTA_PROYECTO,'carga')
#MEDIA_URL='/media/'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@(88aygl@4@trm&y(t03#1r$ab7@cxserf(pn%$&4che@=6x_='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'juegos.apps.principal',
    'captcha',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'juegos.urls'

WSGI_APPLICATION = 'juegos.wsgi.application'


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases
"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':'trivia',
        'USER':'root',
        'PASSWORD':'',
        'HOST':'127.0.0.1',
        'PORT':'3306',
    }
}


# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'es-BO'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL="/media/"

#configuracion de las plantillas
TEMPLATE_DIRS=(os.path.join(RUTA_PROYECTO,"plantillas"),)
#configuracion de los directorios estaticos
STATICFILES_DIRS=(os.path.join(RUTA_PROYECTO,"static"),)
#configuracion del directorio para los archivos multimedia
MEDIA_ROOT=os.path.join(RUTA_PROYECTO,"media")
#para el captcha
RECAPTCHA_PUBLIC_KEY='6LcBaf4SAAAAAD1lhtaSbVF88baC7RZkAfeMVE1b'
RECAPTCHA_PRIVATE_KEY='6LcBaf4SAAAAAOV-My1RjaG1o7MPl0z-bvM_9ce2'