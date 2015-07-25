# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):

    usr = forms.CharField(label="User name")
    pwd = forms.CharField(label="Password", widget=forms.PasswordInput())


class SignupForm(forms.ModelForm):
    """
    Formulario para el modelo Post
    """
    class Meta:
        #password = forms.CharField(widget=forms.PasswordInput)
        model = User
        exclude = ['date_joined','groups','is_active','is_staff','is_superuser','last_login','user_permissions']
        #widgets = {
        #    'password': forms.PasswordInput(),
        #}