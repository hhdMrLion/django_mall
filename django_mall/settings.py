"""
Django settings for django_mall project.

Generated by 'django-admin startproject' using Django 1.11.20.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'p857t5d7koo=c^ya6otq)i*l3x*_-e6h+!5h1ods13ok)k0wt='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 富文本编辑器
    'ckeditor',
    # 'ckeditor_uploader'
    # xadmin
    'xadmin',
    'crispy_forms',
    # 'reversion',
    'accounts.apps.AccountsConfig',  # 用户账户模块
    'mall.apps.MallConfig',  # 商品模块
    'mine.apps.MineConfig',  # 个人模块
    'system.apps.SystemConfig',  # 系统模块
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'utils.middleware.ip_middleware',
    # 'utils.middleware.MallAuthMiddleware'
]

ROOT_URLCONF = 'django_mall.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'system.context_processors.const',
                'mine.context_processors.shop_cart'
            ],
        },
    }
]

WSGI_APPLICATION = 'django_mall.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_mall',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# 自己上传的图片
MEDIA_ROOT = os.path.join(BASE_DIR, 'medias')
MEDIA_URL = '/medias/'

# 使用自定义的用户模型
AUTH_USER_MODEL = 'accounts.User'
LOGIN_URL = '/accounts/user/login/'

CKEDITOR_UPLOAD_PATH = os.path.join(MEDIA_ROOT, 'uploads')

CSRF_USE_SESSIONS = False

# 邮件发送配置
EMAIL_HOST = ''  # smtp.qq.com邮箱服务器
EMAIL_HOST_USER = ''  # 发送邮箱
EMAIL_HOST_PASSWORD = ''  # 邮箱里面开启的授权码

SERVER_EMAIL = ''  # 那个邮箱要发送
ADMINS = [('admin', '')]  # 接收邮箱
# DEBUG 要改为 False  ip那改为’*‘
