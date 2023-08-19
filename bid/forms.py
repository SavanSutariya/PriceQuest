from django import forms
from .models import *
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class AuctionForm(ModelForm):
    class Meta:
        model = Auction
        fields = ['name', 'current_price', 'description','category', 'increment','start_date', 'end_date', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'current_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'increment': forms.NumberInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'start_date': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'end_date': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }
        