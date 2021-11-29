from django.db import models
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.db.models import fields


from userauth.models import Account


class RegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=50)
    first_name = forms.CharField(max_length=40)
    last_name = forms.CharField(max_length=40)
    # not required username
    email = forms.EmailField(max_length=60)

    class Meta:
        model = Account
        fields = ("email", "username", "first_name",
                  "last_name", "password1", "password2")


class AccountAuthenticationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('email', 'password')

    def clean(self):
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']
        if not authenticate(email=email, password=password):
            raise forms.ValidationError("Invalid Email or Password")
