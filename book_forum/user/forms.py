from django import forms
from .models import *
import re
from django.core.exceptions import ValidationError

class RegisterUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email', 'password',]
        widgets = {
            'username': forms.TextInput(attrs={"class": "form-control", 'placeholder':'Книга', 'autocomplete':'off'}),
            'password': forms.PasswordInput(attrs={"class": "form-control", 'placeholder':'Книга', 'autocomplete':'off'}),
            'email': forms.EmailInput(attrs={"class": "form-control", 'placeholder':'Книга', 'autocomplete':'off'}),
        }
    def clean_title(self):
        username = self.cleaned_data['username']
        if re.match('@', username):
            raise ValidationError('Назва не повинна починатись з цифри')
        return username

class LoginUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email', 'password',]
        widgets = {
            'username': forms.TextInput(attrs={"class": "form-control", 'placeholder':'Книга', 'autocomplete':'off'}),
            'password': forms.PasswordInput(attrs={"class": "form-control", 'placeholder':'Книга', 'autocomplete':'off'}),
        }
    def clean_title(self):
        username = self.cleaned_data['username']
        if re.match('@', username):
            raise ValidationError('Назва не повинна починатись з цифри')
        return username

class SettingsUserForm(forms.Form):
    photo = forms.ImageField(required = False, label = 'Фото', widget = forms.FileInput(attrs={"class": "file", 'placeholder': 'Книга', 'onchange':"updatePreview(this, 'image-preview')"}))
    username = forms.CharField(required = False, label = 'Імя',widget = forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Книга', 'autocomplete':'off'}))
    email = forms.EmailField(required = False, label = 'Електронна пошта', widget = forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Книга', 'onchange':"updatePreview(this, 'image-preview')"}))

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username__iexact=username).exists():
           raise ValidationError('Назва не повинна починатись з цифри')
        return username
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email__iexact=email).exists():
           raise ValidationError('Назва не повинна починатись з цифри')
        return email
