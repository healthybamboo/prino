from bs4 import BeautifulSoup
import requests
import datetime


class MovieService:
    def __init__(self):
        pass

    def _get_headers(self):
        return {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        }

    def _get_res(self, url: str):
        headers = self._get_headers()
        sesssion = requests.Session()
        res = sesssion.get(url, headers=headers)
        if res.status_code != 200:
            raise Exception(f'error: {res.status_code}')
        return res

    def get_movie_info(self, url: str):
        res = self._get_res(url)
        soup = BeautifulSoup(res.text, "html.parser")
        title = (
            soup.select_one('title')
            .text.replace('Amazon.co.jp: ', '')
            .replace('を観る | Prime Video', '')
        )
        first_posted = soup.select_one(
            '#av-ep-episodes-0 > div > div._1wFEYz.ci7S35 > div:nth-child(1)'
        ).text
        dt = datetime.datetime.strptime(first_posted, '%Y年%m月%d日')
        first_posted_date = datetime.date(dt.year, dt.month, dt.day)
        rows = soup.select('#tab-content-episodes > div > ol > li')
        episode = ''
        episode_title = ''
        image = ''
        for row in rows:
            if row is None:
                continue
            if row.select_one('a') is None:
                continue
            isAvailablePrime = row.select_one('a').text == 'プライムで観る'

            # primeで見れない場合はスキップ
            if not isAvailablePrime:
                continue
            episode = row.select_one('.izvPPq > span > span:first-child').text
            episode_title = row.select_one(
                '.izvPPq > span > span:last-child'
            ).text
            image = row.select_one('img').get('src')

        if episode == '' or title == '':
            raise Exception('error: episode is empty')

        return episode, episode_title, image, title, first_posted_date
