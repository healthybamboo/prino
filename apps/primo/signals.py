from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Movie
from apps.primo.application import CheckService


@receiver(post_save, sender=Movie)
def listen_post_save(sender, instance, created, **kwargs):
    if created:
        check_service = CheckService()
        check_service.initMovie()
