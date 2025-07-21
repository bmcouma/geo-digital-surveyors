# geodigitalsurveyorsapp/urls.py
from django.urls import path
from . import views

app_name = 'geodigitalsurveyorsapp'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('gallery/', views.gallery, name='gallery'),
    path('contact/', views.contact, name='contact'),
    path('testimonials/', views.testimonials_view, name='testimonials'), 
    path('faqs/', views.faqs_view, name='faqs'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('terms-and-conditions/', views.terms_conditions, name='terms_conditions'),


    
    # Blog URLs
    path('blog/', views.blog_list, name='blog'),
    path('blog/<int:pk>/', views.blog_detail, name='blog_detail'),
    path('blog/<int:pk>/like/', views.blog_like, name='blog_like'),
    path('blog/create/', views.blog_create, name='blog_create'),
    
    # Newsletter subscription
    path('subscribe/', views.subscribe, name='subscribe'),
]