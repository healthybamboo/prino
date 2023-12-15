import logging
import requests
import json
from datetime import datetime
from apps.primo.models import Movie


class NotifyService(object):
    def __init__(self):
        self._logger = logging.getLogger(__name__)
        self._logger.info('NotifyService initialized')

    def notify(self, movies: Movie):
        self._send_discord_notify(movies)

    def _get_headers(self):
        return {
            "Content-Type": "application/json",
        }

    def _send_discord_notify(self, movies: Movie):
        discord_notify_webhook = 'https://discord.com/api/webhooks/1185016466504949860/ixkmEOSfy-13wSQpvEcQJVfmGsPvM4ztuzlG7iFZLLCS-MaMkfGUU25VPnBskFaEH8Yi'
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
