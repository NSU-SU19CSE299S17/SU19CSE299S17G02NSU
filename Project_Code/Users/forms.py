from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# this file  inherits the exisitng register form so that we can add extra fields
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
         model = User
         fields = ['username', 'email', 'password1', 'password2']


