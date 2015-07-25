# -*- coding: utf-8 -*-
from blog.models import Blog
from blog.serializers import BlogSerializer, BlogListSerializer
from blog.views import BlogQueryset
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListCreateAPIView


class BlogListAPI(BlogQueryset, ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogListSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    #search_fields = ('owner__username')
    ordering_fields = ('title')