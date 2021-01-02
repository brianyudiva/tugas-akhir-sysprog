from django import forms
import subprocess

COLOR = [
    ('RGB', 'Color'),
    ('Gray', 'Grayscale'),
]
SIZE = [
    ('A4', 'A4'),
    ('Letter', 'Letter'),
]
QUALITY = [
    ('Draft', 'Draft'),
    ('Normal', 'Normal'),
    ('High', 'High'),
]


class UploadFileForm(forms.Form):
    file = forms.FileField(label='')
    file.widget.attrs['class'] = 'form-control form-control-lg shadow mb-3'
    color = forms.CharField(label='Color Mode: ',
                            widget=forms.Select(choices=COLOR))
    printQuality = forms.CharField(
        label='Print Quality: ', widget=forms.Select(choices=QUALITY))
    pageSize = forms.CharField(
        label='Page size: ', widget=forms.Select(choices=SIZE))
