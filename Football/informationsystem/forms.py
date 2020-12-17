from django.contrib.auth.forms import AuthenticationForm
from django import forms


class CustomQueryForm(forms.Form):
    salary = forms.IntegerField()


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='User name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))