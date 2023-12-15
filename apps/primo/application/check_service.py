import logging
from dateutil.relativedelta import relativedelta
from apscheduler.schedulers.background import BackgroundScheduler
from apps.primo.models import Movie
from .movie_service import MovieService
from .notify_service import NotifyService


class CheckService:
    def __init__(self):
        self._movide_service = MovieService()
        self._notify_service = NotifyService()

    def _fetch(self):
        movies = Movie.objects.all()
        change_movies = []
        for movie in movies:
            if movie.is_active:
                movie.status = 'running'
                movie.save()
                try:
                    (
                        episode,
                        episode_title,
                        image,
                    ) = self._movide_service.get_movie_info(movie.url)
                    if not (
                        movie.episode == episode
                        and movie.episode_title == episode_title
                    ):
                        change_movies.append(movie)
                    movie.status = 'completed'
                    movie.episode = episode
                    movie.episode_title = episode_title
                    movie.image = image
                    movie.save()
                except Exception as e:
                    print(e)
                    movie.status = 'failed'
                    movie.save()
                    continue

        if len(change_movies) > 0:
            self._notify_service.notify(movies=change_movies)

    def initMovie(self):
        movies = Movie.objects.filter(status='pending').all()
        for movie in movies:
            if movie.is_active:
                try:
                    (
                        episode,
                        episode_title,
                        image,
                        title,
                        first_posted_date,
                    ) = self._movide_service.get_movie_info(movie.url)
                    movie.title = movie.title or title
                    movie.episode = movie.episode or episode
                    movie.episode_title = movie.episode_title or episode_title
                    movie.end_at = first_posted_date + relativedelta(months=+3)
                    movie.image = movie.image or image
                    movie.status = 'completed'
                    movie.save()
                except Exception as e:
                    print(e)
                    movie.status = 'failed'
                    movie.save()
                    continue

    def run(self):
        scheduler = BackgroundScheduler()
        scheduler.add_job(
            self._fetch,
            'interval',
            max_instances=1,
            hours=1,
        )
        scheduler.start()
