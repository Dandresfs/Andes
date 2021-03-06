#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Django settings for Andes project.


"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from django.core.urlresolvers import reverse_lazy

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

LOGIN_URL = reverse_lazy('login')
LOGIN_REDIRECT_URL = reverse_lazy('region')
LOGOUT_URL = reverse_lazy('logout')
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+_lb+igq1_@@rdk5bfd-_-(*yx^fow4o-7&=h3e-@^30^@p3s+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'progressbarupload',
    'mixins',
    'django_tables2',
    'rest_framework',
    'django_cleanup',
    'guardian',
    'braces',
    'radicado',
    'area_proyecto',
    'competencia',
    'poblacion',
    'proyectos',
    'participantes',
    'user',
    'region',
    'departamento',
    'municipio',
    'diplomado',
    'area',
    'beneficiario',
    'genero',
    'grado',
    'gestor',
    'financiero',
    'formador',
    'funcionario',
    'eje',
    'pqr',
    'acceso',
    'formacion',
    'administrativo',
    'truchas'
)

REST_FRAMEWORK = {

    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAdminUser',),
    'PAGE_SIZE': 100,
}

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware'
)

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend', # default
    'guardian.backends.ObjectPermissionBackend',
)

ANONYMOUS_USER_ID = -1

ROOT_URLCONF = 'conf.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.core.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'conf.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'sican',
        'USER': 'sican',
        'PASSWORD': '%4nd3s2015%',
        'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
        'PORT': '3306',
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'es-co'

TIME_ZONE = 'America/Bogota'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, "static_files")

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


FILE_UPLOAD_HANDLERS = (
    "django.core.files.uploadhandler.MemoryFileUploadHandler",
    "django.core.files.uploadhandler.TemporaryFileUploadHandler",
    "progressbarupload.uploadhandler.ProgressBarUploadHandler",
)

PROGRESSBARUPLOAD_INCLUDE_JQUERY = False

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'sistemasican@gmail.com'
EMAIL_HOST_PASSWORD = '%4nd3s2015%'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL='Asociación Nacional para el Desarrollo Social - ANDES <sistemasican@gmail.com>'
SERVER_EMAIL = 'sistemasican@gmail.com'
ADMINS = (
    ('Diego', 'sistemas@asoandes.org'),
)

CORS_ORIGIN_ALLOW_ALL = True