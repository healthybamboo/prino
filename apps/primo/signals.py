from dateutil.relativedelta import relativedelta
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Movie
from apps.primo.application.movie_service import MovieService
from apps.primo.application import NotifyService

movie_service = MovieService()
notify_service = NotifyService()


@receiver(post_save, sender=Movie)
def listen_post_save(sender, instance, created, **kwargs):
    if created:
        movie = instance
        try:
            (
                episode,
                episode_title,
                image,
                title,
                first_posted_date,
            ) = movie_service.get_movie_info(movie.url)
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
        notify_service.send_register_message(movie)
