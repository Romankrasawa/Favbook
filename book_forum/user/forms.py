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

class SettingsUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['photo']
        widgets = {
            'photo': forms.FileInput(attrs={"class": "file", 'placeholder': 'Книга', 'onchange':"updatePreview(this, 'image-preview')"}),
        }
    def clean_title(self):
        username = self.cleaned_data['username']
        if re.match('@', username):
            raise ValidationError('Назва не повинна починатись з цифри')
        return username