# -*- coding: utf-8 -*-
from blog.models import Blog
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import logout as django_logout, authenticate, login as django_login
from users.forms import LoginForm, SignupForm
from django.views.generic import View


class LoginView(View):

    def get(self, request):
        error_messages = []
        form = LoginForm()
        context = {
            'errors': error_messages,
            'login_form': form
        }
        return render(request, 'users/login.html', context)

    def post(self, request):
        error_messages = []
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('usr')
            password = form.cleaned_data.get('pwd')
            user = authenticate(username=username, password=password)
            if user is None:
                error_messages.append('Nombre de usuario o contraseña incorrectos')
            else:
                if user.is_active:
                    django_login(request, user)
                    url = request.GET.get('next',
                                          'post_home')  # si no existe el parámetro GET 'next', le mandamos a 'photos_home'
                    return redirect(url)
                else:
                    error_messages.append('El usuario no está activo')
        context = {
            'errors': error_messages,
            'login_form': form
        }
        return render(request, 'users/login.html', context)


class LogoutView(View):

    def get(self, request):
        if request.user.is_authenticated():
            django_logout(request)
        return redirect('post_home')


class SignupView(View):

    def get(self, request):
        """
        Muesta un formulario para crear un user
        :param request: HttpRequest
        :return: HttpResponse
        """
        form = SignupForm()
        context = {
            'form': form,
            'success_message': ''
        }
        return render(request, 'users/new_user.html', context)

    def post(self, request):
        """
        Crea un user en base a la información POST
        :param request: HttpRequest
        :return: HttpResponse
        """
        success_message = ''

        form = SignupForm(request.POST)
        if form.is_valid():
            user = User()
            user.username = form.cleaned_data.get('usr')
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            user.email = form.cleaned_data.get('email')
            user.set_password(form.cleaned_data.get('password'))
            user.save()

            blog = Blog()
            blog.title = "My first blog"
            blog.owner = user
            blog.save()

            success_message = 'Creado con éxito!'
            success_message += '<a href="{0}">'.format(
                reverse('post_home', args=[])
            )
            success_message += 'go Home!'
            success_message += '</a>'
        context = {
            'form': form,
            'success_message': success_message
        }
        return render(request, 'users/new_user.html', context)
