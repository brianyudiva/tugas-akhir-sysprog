from django.shortcuts import render
from .forms import UploadFileForm
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import subprocess

def index(request):
  printer = subprocess.check_output(['lpstat','-p']).decode().split()[1]
  if request.method == 'POST':
    form = UploadFileForm(request.POST, request.FILES)
    if form.is_valid():
      call_bash(request.FILES['file'], printer)
  else:
    form = UploadFileForm()
  return render(request, 'index.html', {'form' : form, 'printer' : printer })

def call_bash(file, print):
  fs = FileSystemStorage()
  filename = fs.save(file.name, file)
  abs_path = settings.MEDIA_ROOT + "/" + filename
  subprocess.Popen(['lp','-d',print,abs_path])
  return


