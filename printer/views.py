from django.shortcuts import render
from .forms import UploadFileForm
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import subprocess


def index(request):
    printer = subprocess.check_output(['lpstat', '-p']).decode().split()[1]
    options = subprocess.check_output(
        ['lpoptions', '-l']).decode().split()
    print(options)
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            color_mode = request.POST.get('color', 'RGB')
            print_quality = request.POST['printQuality']
            page_size = request.POST['pageSize']
            print(color_mode, print_quality, page_size)
            call_bash(request.FILES['file'], printer, color_mode, print_quality, page_size)
    else:
        form = UploadFileForm()
    return render(request, 'index.html', {'form': form, 'printer': printer})


def call_bash(file, print, color_mode, print_quality, page_size):
    fs = FileSystemStorage()
    filename = fs.save(file.name, file)
    abs_path = settings.MEDIA_ROOT + "/" + filename
    color = "ColorModel=" + color_mode
    quality = "Print=" + print_quality
    size = "PageSize=" + page_size
    subprocess.Popen(['lp', '-d', print, '-o', color, '-o', quality, '-o', size, abs_path])
    return
