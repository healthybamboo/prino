from .base import *

import os

# DebugモードをFalseに設定
DEBUG = False

# 環境変数から取得する設定(必須)
ENVIROMENT_PROPS = {
    'DB_HOST': os.environ.get('DB_HOST'),
    'DB_PORT': os.environ.get('DB_PORT'),
    'DB_NAME': os.environ.get('DB_NAME'),
    'DB_USER': os.environ.get('DB_USER'),
    'DB_PASSWORD': os.environ.get('DB_PASSWORD'),
    'WEBHOOK_URL': os.environ.get('WEBHOOK_URL'),
    'APP_SECRET': os.environ.get('APP_SECRET'),
}


for key, value in ENVIROMENT_PROPS.items():
    if value is None:
        raise ValueError(f'{key} is not set in enviroment variables.')


ALLOWED_HOSTS = [
    'prino.bamgrove.net',
    'localhost',
    r'^10\.',
    r'^172\.(1[6-9]|2[0-9]|3[0-1])\.',
    r'^192\.168\.',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': ENVIROMENT_PROPS['DB_HOST'],
        'PORT': ENVIROMENT_PROPS['DB_PORT'],
        'NAME': ENVIROMENT_PROPS['DB_NAME'],
        'USER': ENVIROMENT_PROPS['DB_USER'],
        'PASSWORD': ENVIROMENT_PROPS['DB_PASSWORD'],
    }
}

SECRET_KEY = ENVIROMENT_PROPS['APP_SECRET']
