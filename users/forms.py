# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):

    usr = forms.CharField(label="User name")
    pwd = forms.CharField(label="Password", widget=forms.PasswordInput())


class SignupForm(forms.Form):
    """
    Formulario para el modelo User
    """

    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")
    email = forms.CharField(label="Email")
    usr = forms.CharField(label="User")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
