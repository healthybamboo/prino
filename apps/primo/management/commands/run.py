import sys
from typing import Any
import sqlite3
from django.core.management.base import LabelCommand
from apps.primo.application import CheckService


class Command(LabelCommand):
    def __init__(self):
        self._check_service = CheckService()

    def _fetch(self):
        print('fetch')
        self._check_service._fetch()

    def _data_change(self):
        print('data change')
        dbname = 'db.sqlite3'
        conn = sqlite3.connect(dbname)
        cur = conn.cursor()
        cur.execute(
            'UPDATE primo_movie SET episode = "test" WHERE is_active = 1'
        )
        conn.commit()
        conn.close()
        print('ok')

    def handle_label(self, label: Any, **options: Any) -> None:
        if label == 'fetch':
            self._fetch()
        elif label == 'dc':
            self._data_change()
