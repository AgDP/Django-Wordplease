# -*- coding: utf-8 -*-
from blog.models import Blog
from django.contrib.auth.models import User
from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.views.generic import View
from post.models import Post
from post.views import PostQueryset


class BlogQueryset(object):

    def get_blogs_queryset(self, pk):
        user = User.objects.filter(username=pk)
        blogs = Blog.objects.filter(owner=user)
        return blogs

class BlogsListView(View):
    def get(self, request):
        """
        Esta función devuelve la lista de blogs
        """
        blogs = Blog.objects.all()
        context = {
            'blog_list': blogs[:5]
        }
        return render(request, 'blog/list_blogs.html', context)


class DetailBlogView(View, BlogQueryset, PostQueryset):

    def get(self, request, pk):
        """
        Carga la página de detalle de un blog
        :param request: HttpRequest
        :param pk: id del blog
        :return: HttpResponse
        """
        possible_blogs = self.get_blogs_queryset(pk).all()

        blog = possible_blogs[0] if len(possible_blogs) >= 1 else None
        if blog is not None:

            posts = Post.objects.filter(blog=blog).order_by('-posted_date')
            context = {
                'post_list': posts
            }
            return render(request, 'blog/detail.html', context)
        else:
            return HttpResponseNotFound('No existe el blog')  # 404 not found