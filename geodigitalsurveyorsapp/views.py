# Create your views here.

from django.shortcuts import render
from .models import Service
from .models import GalleryImage
from django.contrib import messages
from .forms import ContactForm

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

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent successfully.")
            form = ContactForm()  # reset form
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

