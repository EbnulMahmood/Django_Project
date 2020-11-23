from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Audio(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    artist = models.CharField(max_length=100)
    lyrics = models.TextField(null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    audio_file = models.FileField(upload_to='audio_files')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('music-detail', kwargs={'pk': self.pk})