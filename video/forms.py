from django import forms
from .models import Video


class VideoUpdateForm(forms.ModelForm):

    class Meta:
        model = Video
        fields = [
        'title',
        'artist',
        'lyrics',
        'video_file'
        ]