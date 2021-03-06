# -*- coding: utf-8 -*-
"""
Django settings for product project.

Generated by 'django-admin startproject' using Django 1.8.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import tempfile
from mako.lookup import TemplateLookup
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = BASE_DIR

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'z3=k0k3jg$(x1hlm5oqp29-cx%n$q_3h@4hnnl@3iht8k8o^o0'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = (
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'djangomako',
    'banner',
    'cms',
    'django_cleanup',
    'DjangoUeditor',
    'gunicorn'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    # 'djangomako.middleware.MakoMiddleware',
)

ROOT_URLCONF = 'web.urls'

MAKO_MODULE_DIR = os.path.join(tempfile.gettempdir(),'oce')
MAKO_TEMPLATE_DIRS = os.path.join(PROJECT_ROOT, 'templates')
DJANGO_TEMPLATE_DIRS = os.path.join(PROJECT_ROOT, 'templates')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
    },
    {
        'BACKEND': 'djangomako.backends.MakoBackend',
        'NAME': 'mako',
        'DIRS': [MAKO_TEMPLATE_DIRS,DJANGO_TEMPLATE_DIRS],
    },
]

print( os.path.join(BASE_DIR, 'templates/mako'))

WSGI_APPLICATION = 'web.wsgi.application'

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
)

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "HOST": "localhost",
        "USER": "root",
        "NAME": "oce",
        "PASSWORD": "root",
        "PORT": "",
    },
}

# 每页显示10
PAGE_NUM = 10

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/
# 后台主题设置
LANGUAGE_CODE = 'zh-CN'
TIME_ZONE = 'Asia/Shanghai'
USE_I18N = True
USE_L10N = False
USE_TZ = False

SUIT_CONFIG = {
    'ADMIN_NAME': '六博光电后台管理系统',
    'HEADER_DATE_FORMAT': 'l, j. F Y',  # Saturday, 16th March 2013
    'HEADER_TIME_FORMAT': 'H:i',  # 18:42
    # forms
    'SHOW_REQUIRED_ASTERISK': True,  # Default True
    'CONFIRM_UNSAVED_CHANGES': True,  # Default True

    # menu
    'SEARCH_URL': '/admin/auth/user/',
    'MENU_ICONS': {
        'sites': 'icon-leaf',
        'auth': 'icon-lock',
    },
    'MENU_OPEN_FIRST_CHILD': True,  # Default True
    'MENU_EXCLUDE': ('auth.group',),
    'MENU': (
        'sites',
        {'label': 'Settings', 'icon': 'icon-cog',
         'models': ('auth.user', 'auth.group')},
        {'label': 'Support', 'icon': 'icon-question-sign', 'url': '/support/'},
    ),

    'LIST_PER_PAGE': 15
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = '/static'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

# 文件存储路径
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "/media")
