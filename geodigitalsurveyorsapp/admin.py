# Register your models here.

from django.contrib import admin
from .models import Service
from .models import GalleryImage
from .models import ContactMessage
from .models import Testimonial

admin.site.register(Service)
admin.site.register(GalleryImage)
admin.site.register(ContactMessage)
admin.site.register(Testimonial)




