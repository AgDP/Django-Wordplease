# -*- coding: utf-8 -*-
"""wordplease URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from blog.api import BlogListAPI
from blog.views import BlogsListView, DetailBlogView
from django.conf.urls import include, url
from django.contrib import admin
from post.api import PostListAPI, PostDetailAPI, PostCreateAPI
from post.views import HomeView, DetailPostView, CreatePostView
from users.api import UserListAPI, UserDetailAPI
from users.views import LoginView, LogoutView, SignupView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='post_home'),
    url(r'^admin/', include(admin.site.urls)),

    # Post
    url(r'^new-post/$', CreatePostView.as_view(), name='create_post'),

    # Blogs de usuarios
    url(r'^blogs/$', BlogsListView.as_view(), name='blog_list'),
    url(r'^blogs/(?P<pk>[-\w]+)/$', DetailBlogView.as_view(), name='blog_detail'),
    url(r'^blogs/(?P<pk>[-\w]+)/(?P<idPost>[0-9]+)/$', DetailPostView.as_view(), name='post_detail'),

    # Users URLS
    url(r'^login$', LoginView.as_view(), name='users_login'),
    url(r'^logout$', LogoutView.as_view(), name='users_logout'),
    url(r'^singup$', SignupView.as_view(), name='users_singup'),

    # API Users URLs
    url(r'^api/1.0/users/$', UserListAPI.as_view(), name='user_list_api'),
    url(r'^api/1.0/users/(?P<pk>[0-9]+)$', UserDetailAPI.as_view(), name='user_detail_api'),

    # API Blogs URLs
    url(r'^api/1.0/blogs/$', BlogListAPI.as_view(), name='blog_list_api'),

    # API Post URLs
    url(r'^api/1.0/blogs/(?P<pk>[0-9]+)/$', PostListAPI.as_view(), name='post_list_api'),
    url(r'^api/1.0/posts/(?P<pk>[0-9]+)/$', PostDetailAPI.as_view(), name='post_detail_api'),
    url(r'^api/1.0/posts/$', PostCreateAPI.as_view(), name='post_create_api'),
]
