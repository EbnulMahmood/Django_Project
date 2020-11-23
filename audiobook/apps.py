from django.apps import AppConfig


class AudiobookConfig(AppConfig):
    name = 'audiobook'

    def ready(self):
        import audiobook.signals
