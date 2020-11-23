from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Video(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    artist = models.CharField(max_length=100)
    lyrics = models.TextField(null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    video_file = models.FileField(upload_to='video_files')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('video-detail', kwargs={'pk': self.pk})