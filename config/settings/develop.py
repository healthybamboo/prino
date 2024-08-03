from .base import *

DISCORD_WEBHOOK_URL = 'https://discord.com/api/webhooks/xxxxxxxxxxxxx'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': 'host.docker.internal',
        'PORT': '5432',
        'NAME': 'prino',
        'USER': 'postgres',
        'PASSWORD': 'password',
    }
}
