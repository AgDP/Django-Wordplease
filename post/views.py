# -*- coding: utf-8 -*-
from blog.views import Blog
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import View
from post.forms import PostForm
from post.models import Post

class PostQueryset(object):

    def get_post_queryset(self, request):
        posts = Post.objects.all()
        return posts

class HomeView(View):

    def get(self, request):
        """
        Esta función devuelve el home de mi página
        """
        posts = Post.objects.all().order_by('-posted_date')
        context = {
            'post_list': posts[:5]
        }
        return render(request, 'post/home.html', context)


class DetailPostView(View, PostQueryset):

    def get(self, request, pk, idPost):
        """
        Carga la página de detalle de un post
        :param request: HttpRequest
        :param pk: id del post
        :return: HttpResponse
        """

        possible_posts = self.get_post_queryset(request).filter(pk=idPost)

        post = possible_posts[0] if len(possible_posts) >= 1 else None
        if post is not None:
            # cargar la plantilla de detalle
            context = {
                'post': post
            }
            return render(request, 'post/detail.html', context)
        else:
            return HttpResponseNotFound('No existe el post')  # 404 not found


class CreatePostView(View):

    @method_decorator(login_required())
    def get(self, request):
        """
        Muesta un formulario para crear un post
        :param request: HttpRequest
        :return: HttpResponse
        """
        form = PostForm()
        context = {
            'form': form,
            'success_message': ''
        }
        return render(request, 'post/new_post.html', context)

    @method_decorator(login_required())
    def post(self, request):
        """
        Crea un post en base a la información POST
        :param request: HttpRequest
        :return: HttpResponse
        """
        success_message = ''
        post_with_owner = Post()
        blog = self.get_blogs_queryset(request.user.username).all()
        post_with_owner.blog = blog[0]
        post_with_owner.owner = request.user  # asigno como propietario de la foto, el usuario autenticado
        form = PostForm(request.POST, instance=post_with_owner)
        if form.is_valid():
            new_post = form.save()  # Guarda el objeto Photo y me lo devuelve
            form = PostForm()
            success_message = 'Guardado con éxito!'
            success_message += '<a href="{0}">'.format(
                reverse('post_detail', args=[new_post.blog.owner.username, new_post.pk])
            )
            success_message += 'Ver post'
            success_message += '</a>'
        context = {
            'form': form,
            'success_message': success_message
        }
        return render(request, 'post/new_post.html', context)

    def get_blogs_queryset(self, pk):
        user = User.objects.filter(username=pk)
        blogs = Blog.objects.filter(owner=user)
        return blogs