import logging
import requests
import json
from datetime import datetime
from django.conf import settings
from apps.primo.models import Movie


class NotifyService(object):
    def __init__(self):
        pass

    def notify(self, movies: Movie):
        self._send_discord_notify(movies)

    def _get_headers(self):
        return {
            "Content-Type": "application/json",
        }

    def _send_discord_notify(self, movies: Movie):
        discord_notify_webhook = settings.DISCORD_WEBHOOK_URL
        headers = self._get_headers()
        print('send_discord_notify')

        body = {
            "username": "prino",
            "content": "## 🤖 アニメ更新通知",
            "embeds": [
                (
                    {
                        "title": movie.title + ":" + movie.episode,
                        "description": movie.episode_title,
                        "url": movie.url,
                        "image": {
                            "url": movie.image,
                        },
                    }
                )
                for movie in movies
            ],
        }
        res = requests.post(
            discord_notify_webhook, data=json.dumps(body), headers=headers
        )
