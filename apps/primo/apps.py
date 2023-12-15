from django.apps import AppConfig


class PrimoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.primo'

    def ready(self) -> None:
        import apps.primo.signals
        from apps.primo.application import CheckService

        check_service = CheckService()
        check_service.run()
