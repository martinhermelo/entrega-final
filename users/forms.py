from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class User_registration_form(UserCreationForm):
    email= forms.EmailField(required=True)
    password1= forms.CharField(label= "Password", widget=forms.PasswordInput)
    password2= forms.CharField(label= "Password confirmation", widget=forms.PasswordInput)

    last_name= forms.CharField()
    first_name= forms.CharField()

    class Meta:
        model= User
        fields= {"username", "email", "password1", "password2","last_name", "first_name"}

        help_texts = {k: "" for k in fields}