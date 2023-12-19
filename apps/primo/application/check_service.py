import logging
import time
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
                        _,
                        _,
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
                    self._notify_service.send_error_message(str(e), movie)
                    print(e)
                    movie.status = 'failed'
                    movie.save()
                    continue
            time.sleep(5)

        if len(change_movies) > 0:
            self._notify_service.send_update_message(movies=change_movies)

    def run(self):
        scheduler = BackgroundScheduler()
        scheduler.add_job(
            self._fetch,
            'interval',
            max_instances=1,
            hours=1,
        )
        scheduler.start()
