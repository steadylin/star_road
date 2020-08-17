# 上线的配置

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(BASE_DIR)
import sys

# print(sys.path)
sys.path.insert(0, BASE_DIR)
# 把apps的路径加入到环境变量
sys.path.insert(1, os.path.join(BASE_DIR, 'apps'))
# print(sys.path)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'xoz4x6tg@rv$1k9qf$oas3xq146sy2&=ay5n48=d10h#^j-aw5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_jwt',

    'corsheaders',
    # xadmin主体模块
    'xadmin',
    # 渲染表格模块
    'crispy_forms',
    # 为模型通过版本控制，可以回滚数据
    'reversion',

    'user',  # 因为apps目录已经被加到环境变量了，所以直接能找到
    'home',
    'video',
    'img',
    'order',
    'film',
]

MIDDLEWARE = [
#    'star_roadapi.utils.middle.MyMiddle',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

from corsheaders.middleware import CorsMiddleware
ROOT_URLCONF = 'star_roadapi.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'star_roadapi.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'star_roadapi',
        'USER': 'star_roadapi',
        'PASSWORD': 'Luffy123?',
        'HOST': '127.0.0.1',
        'PORT': 3306
    },
}

import pymysql

pymysql.install_as_MySQLdb()
# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

AUTH_USER_MODEL = 'user.User'
# 开放头像地址
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# 日志配置
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(lineno)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(module)s %(lineno)d %(message)s'
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console': {
            # 实际开发建议使用WARNING
            'level': 'WARNING',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'file': {
            # 实际开发建议使用ERROR
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            # 日志位置,日志文件名,日志保存目录必须手动创建，注：这里的文件路径要注意BASE_DIR代表的是小luffyapi
            'filename': os.path.join(os.path.dirname(BASE_DIR), "logs", "star_road.log"),
            # 日志文件的最大值,这里我们设置300M
            'maxBytes': 300 * 1024 * 1024,
            # 日志文件的数量,设置最大日志数量为10
            'backupCount': 100,
            # 日志格式:详细格式
            'formatter': 'verbose',
            # 文件内容编码
            'encoding': 'utf-8'
        },
    },
    # 日志对象
    'loggers': {
        'django': {
            'handlers': ['console', 'file'],
            'propagate': True,  # 是否让日志信息继续冒泡给其他的日志处理系统
        },
    }
}

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
    'VIEW',
)
CORS_ALLOW_HEADERS = (
    'authorization',
    'content-type',
)


# STATICFILES_DIRS = ( os.path.join(BASE_DIR, r'star_roadapi\libs\bdface\static') )
# print(STATICFILES_DIRS)



from .const import *
import datetime

REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'utils.exceptions.common_exception_handler',
    # 短信发送频率限制的key
    'DEFAULT_THROTTLE_RATES': {'sms': '1/m'},  # key要跟类中的scop对应
    # 自定义jwt认证类
    'DEFAULT_AUTHENTICATION_CLASSES': ('utils.authentication.MyAuthentication',),
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=7),  # token过期时间，手动配置
    # 每页显示条数
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',  # 添加这一行解决，
#    'PAGE_SIZE': 10,
}

# django默认不支持redis做缓存
# from django.core.cache.backends.filebased import FileBasedCache
# from django_redis.cache import RedisCache
# 缓存
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "CONNECTION_POOL_KWARGS": {"max_connections": 100}
            # "PASSWORD": "123",
        }
    }
}
# 修改static配置，新增STATIC_ROOT
STATIC_URL = '/static/'
STATIC_ROOT = '/home/project/star_roadapi/star_roadapi/static'
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)

# 上线后要换成公网地址
# 后台基URL
BASE_URL = 'http://39.97.209.187:8000'
# 前台基URL
STAR_ROAD_URL = 'http://39.97.209.187'
# 支付宝同步异步回调接口配置
# 后台异步回调接口
NOTIFY_URL = BASE_URL + "/order/success/"
# 前台同步回调接口，没有 / 结尾
RETURN_URL = STAR_ROAD_URL + "/pay/success"
