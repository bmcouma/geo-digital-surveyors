# Register your models here.

from django.contrib import admin
from .models import Service
from .models import GalleryImage


admin.site.register(Service)
admin.site.register(GalleryImage)
