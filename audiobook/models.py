from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse


class PDF(models.Model):
    title = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    summary = models.TextField(null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    pdf_file = models.FileField(upload_to='pdf_files')
    image = models.ImageField(default='default_pdfImage.jpg', upload_to='pdf_images')
    audio_file = models.FileField(null = True, upload_to='pdf_audios')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('audiobook-detail', kwargs={'pk': self.pk})