import os
import re
from bs4 import BeautifulSoup
import pytest
import pickle
from django.test import client
from django.core.management import call_command
from django.urls import resolve
from django.contrib.admin import AdminSite

DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')


@pytest.fixture
def soup_fixture():
    file_path = os.path.join(DATA_DIR, 'osinoko_soup.pkl')
    with open(file_path, 'rb') as f:
        return pickle.load(f)


def test_can_get_movie_title(soup_fixture):
    # setup
    soup: BeautifulSoup = soup_fixture

    # タイトルを取得
    title = (
        soup.select_one('title')
        .text.replace('Amazon.co.jp: ', '')
        .replace('を観る | Prime Video', '')
    )

    assert title == '【推しの子】第2期'


def test_can_get_first_posted_date(soup_fixture):
    # setup
    soup: BeautifulSoup = soup_fixture

    # 最初に配信された日付を取得
    first_episode = soup.select_one('#av-ep-episodes-0')

    # 正規表現でyyyy年mm月dd日の形式のデータを取得
    first_posted = re.search(
        r'\d{4}年\d{1,2}月\d{1,2}日', first_episode.text
    ).group()

    assert first_posted == '2024年7月3日'
