from django import forms
from .models import *
import re
from django.core.exceptions import ValidationError
from .services import *

import logging

logger = logging.getLogger(__name__)

class RegisterUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email', 'password',]
        widgets = {
            'username': forms.TextInput(attrs={"class": "form-control", 'placeholder':'Книга', 'autocomplete':'off'}),
            'password': forms.PasswordInput(attrs={"class": "form-control", 'placeholder':'Книга', 'autocomplete':'off'}),
            'email': forms.EmailInput(attrs={"class": "form-control", 'placeholder':'Книга', 'autocomplete':'off'}),
        }

    def __init__(self, *args, **kwargs):
        self.request=kwargs.get('request',None)
        if self.request != None:
            del kwargs['request']
        super(RegisterUserForm, self).__init__(*args, **kwargs)

    def clean_title(self):
        return validate_user_username(self)

class LoginUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email', 'password',]
        widgets = {
            'username': forms.TextInput(attrs={"class": "form-control", 'placeholder':'Книга', 'autocomplete':'off'}),
            'password': forms.PasswordInput(attrs={"class": "form-control", 'placeholder':'Книга', 'autocomplete':'off'}),
        }

class SettingsUserForm(forms.Form):
    photo = forms.ImageField(required = False, label = 'Фото', widget = forms.FileInput(attrs={"class": "file", 'placeholder': 'Книга', 'onchange':"updatePreview(this, 'image-preview')"}))
    username = forms.CharField(required = False, label = 'Імя',widget = forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Книга', 'autocomplete':'off'}))
    email = forms.EmailField(required = False, label = 'Електронна пошта', widget = forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Книга', 'onchange':"updatePreview(this, 'image-preview')"}))

    def __init__(self, *args, **kwargs):
        self.request=kwargs.get('request',None)
        if self.request != None:
            del kwargs['request']
        super(SettingsUserForm, self).__init__(*args, **kwargs)

    def clean_username(self):
        return validate_user_username(self)
        
    def clean_email(self):
        email = self.cleaned_data['email']
        if email != self.request.user.email and User.objects.filter(email__iexact=email).exists():
           raise ValidationError('Назва не повинна починатись з цифри')
        return email
