from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField(label='')
    file.widget.attrs['class'] = 'form-control form-control-lg shadow'