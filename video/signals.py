import os
from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import Video


def _delete_file(path):
    if os.path.isfile(path):
       os.remove(path)

@receiver(post_delete, sender=Video)
def delete_file(sender, instance, *args, **kwargs):
    if instance.video_file:
        _delete_file(instance.video_file.path)