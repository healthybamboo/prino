import logging
import requests
import json
from datetime import datetime
from django.conf import settings
from apps.primo.models import Movie


class NotifyService(object):
    def __init__(self):
        self._webhook_url = settings.DISCORD_WEBHOOK_URL
        self._headers = {
            "Content-Type": "application/json",
        }

    def _send_message(self, data):
        res = requests.post(
            self._webhook_url, headers=self._headers, data=json.dumps(data)
        )
        return res

    def send_register_message(self, movie: Movie):
        print('send_register_message')

        body = {
            "username": "prino",
            "content": f'## 🤖 監視対象の追加\n{movie.title}を追加\n{movie.url}',
        }
        res = self._send_message(body)
        print(res)

    def send_error_message(self, error: str, movie: Movie):
        print('send_error_message')

        body = {
            "username": "prino",
            "content": f'## 🤖 エラー報告\n{movie.title}\n{error}',
        }
        res = self._send_message(body)
        print(res)

    def send_update_message(self, movies: Movie):
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
        print(body)
        res = self._send_message(body)
        print(res)
