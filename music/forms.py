from django import forms
from .models import Audio


class AudioUpdateForm(forms.ModelForm):

    class Meta:
        model = Audio
        fields = [
        'title',
        'artist',
        'lyrics',
        'audio_file'
        ]