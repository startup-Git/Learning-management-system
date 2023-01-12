from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.forms import ValidationError
from django.contrib import messages
from django.shortcuts import redirect
from requests import request

class RegistationForm(UserCreationForm):
    first_name = forms.CharField(label='First Name', required=True, widget=forms.TextInput(attrs={'class':'form-control mb-3'}))
    last_name = forms.CharField(label='Last Name', required=True, widget=forms.TextInput(attrs={'class':'form-control mb-3'}))
    username = forms.CharField(label='User Name', required=True, widget=forms.TextInput(attrs={'class':'form-control mb-3'}))
    email = forms.EmailField(label='E-mail', required=True, widget=forms.EmailInput(attrs={'class':'form-control mb-3'}))
    password1 = forms.CharField(label='Password', required=True, widget=forms.PasswordInput(attrs={'class':'form-control mb-3'}))
    password2 = forms.CharField(label='Confirm Password', required=True, widget=forms.PasswordInput(attrs={'class':'form-control mb-3'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    username = UsernameField(label='User Name', required=True, widget=forms.TextInput(attrs={'class':'form-control mb-3'}))
    password = forms.CharField(label='Password', required=True, widget=forms.PasswordInput(attrs={'class':'form-control mb-3', 'autocomplete':'current-password'}))

class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label='Old password', widget=forms.PasswordInput(attrs={'autofocus':'True', 'class':'form-control mb-3', 'autocomplete':'current-password'}))
    new_password1 = forms.CharField(label='New password', widget=forms.PasswordInput(attrs={'autofocus':'True', 'class':'form-control mb-3', 'autocomplete':'current-password'}))
    new_password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput(attrs={'autofocus':'True', 'class':'form-control mb-3', 'autocomplete':'current-password'}))

class MyPasswordResetForm(PasswordResetForm):
    email  = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control mb-3'}))

class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label='New password', widget=forms.PasswordInput(attrs={'autofocus':'True', 'class':'form-control mb-3', 'autocomplete':'current-password'}))
    new_password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput(attrs={'autofocus':'True', 'class':'form-control mb-3', 'autocomplete':'current-password'}))

