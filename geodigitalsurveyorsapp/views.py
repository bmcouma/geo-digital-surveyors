# Create your views here.

from django.shortcuts import render
from .models import Service
from .models import GalleryImage

def services(request):
    service_list = Service.objects.all().order_by('-created_at')
    return render(request, 'services.html', {'services': service_list})

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def gallery(request):
    return render(request, 'gallery.html')

def contact(request):
    return render(request, 'contact.html')

def gallery(request):
    images = GalleryImage.objects.all().order_by('-uploaded_at')
    return render(request, 'gallery.html', {'images': images})
