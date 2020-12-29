from django.shortcuts import render
from .forms import UploadFileForm
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import subprocess

def index(request):
  if request.method == 'POST':
    form = UploadFileForm(request.POST, request.FILES)
    if form.is_valid():
      call_bash(request.FILES['file'])
  else:
    form = UploadFileForm()
  return render(request, 'index.html', {'form' : form})

def call_bash(file):
  fs = FileSystemStorage()
  filename = fs.save(file.name, file)
  print(settings.MEDIA_ROOT + "\\" + filename)
  # subprocess.Popen(['printer.sh', abs_path])
  return


