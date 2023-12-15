from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Movie
from apps.primo.application import CheckService
from apps.primo.application import NotifyService

check_service = CheckService()
notify_service = NotifyService()


@receiver(post_save, sender=Movie)
def listen_post_save(sender, instance, created, **kwargs):
    if created:
        check_service.initMovie()
        notify_service.send_register_message(instance)
