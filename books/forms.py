from django import forms
from books.models import Books
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class BookModelForm(forms.ModelForm):
    class Meta():
        model=Books
        fields='__all__'
        
class RegistrationForm(forms.ModelForm):
    class Meta():
        model=User
        fields=["username","email","password"]
        
class LogInForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()