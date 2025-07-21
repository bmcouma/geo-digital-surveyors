from django import forms
from .models import ContactMessage
from .models import Testimonial

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['full_name', 'phone', 'email', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 4}),
        }

class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['client_name', 'role', 'message']
        widgets = {
            'client_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'role': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Title (optional)'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your feedback...', 'rows': 4}),
        }
