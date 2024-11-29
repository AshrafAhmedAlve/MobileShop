from django import forms
from .models import Mobile

class MobileForm(forms.ModelForm):
    class Meta:
        model = Mobile
        fields = ['name', 'brand', 'price', 'stock', 'image']  # Fields to include in the form
