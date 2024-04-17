from django import forms
from django.forms import ModelForm
from .models import Book

class HelloForm(forms.Form):
    nom = forms.CharField(max_length=10)
    message = forms.CharField(widget=forms.Textarea)


class Create_books_form(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'