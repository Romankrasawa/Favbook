from django import forms
from .models import *
import re
from django.core.exceptions import ValidationError


class CreateBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['cover','title', 'description', 'author', 'year', 'category', 'status']
        widgets = {
            'cover': forms.FileInput(attrs={"class": "file", 'placeholder': 'Книга', 'onchange':"updatePreview(this, 'image-preview')"}),
            'title': forms.TextInput(attrs={"class": "form-control", 'placeholder':'Книга'}),
            'description': forms.Textarea(attrs={"class": "form-control", 'rows':'2', 'placeholder':'Книга'}),
            'author': forms.TextInput(attrs={"class": "form-control", 'placeholder':'Книга'}),
            'year': forms.DateInput(attrs={"class": "form-control", 'placeholder':'Книга'}),
            'status': forms.Select(attrs={"class": "form-control", 'placeholder':'Книга'}),
            'category': forms.SelectMultiple(attrs={"class": "form-control", 'placeholder':'Книга'})
        }
    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match('#', title):
            raise ValidationError('Назва не повинна починатись з цифри')
        return title

class CreateDiscussionForm(forms.ModelForm):
    class Meta:
        model = Discussion
        fields = ['book','title', 'description']
        widgets = {
            'book': forms.Select(attrs={"class": "form-control", 'placeholder': 'Книга'}),
            'title': forms.TextInput(attrs={"class": "form-control", 'placeholder':'Книга'}),
            'description': forms.Textarea(attrs={"class": "form-control", 'rows':'2', 'placeholder':'Книга'}),
            'status': forms.Select(attrs={"class": "form-control", 'placeholder':'Книга'}),
        }
    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match('#', title):
            raise ValidationError('Назва не повинна починатись з цифри')
        return title

class AnswerDiscussion_commentForm(forms.ModelForm):
    class Meta:
        model = Discussion_comment
        fields = ['content', 'answer']
        widgets = {
            'content': forms.Textarea(attrs={"class": "form-control", 'rows': '2', 'placeholder': 'Книга'}),
            'answer': forms.HiddenInput()
        }
class CreateDiscussion_commentForm(forms.ModelForm):
    class Meta:
        model = Discussion_comment
        fields = ['content',]
        widgets = {
            'content': forms.Textarea(attrs={"class": "form-control", 'rows': '2', 'placeholder': 'Книга'}),
        }
class CreateBook_commentForm(forms.ModelForm):
    class Meta:
        model = Book_comment
        fields = ['content',]
        widgets = {
            'content': forms.Textarea(attrs={"class": "form-control", 'rows': '2', 'placeholder': 'Книга'}),
        }