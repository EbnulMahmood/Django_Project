from django import forms
from .models import PDF


class PDFUpdateForm(forms.ModelForm):

    class Meta:
        model = PDF
        fields = [
        'title',
        'author',
        'summary',
        'pdf_file'
        ]