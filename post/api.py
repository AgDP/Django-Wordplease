# -*- coding: utf-8 -*-
from blog.models import Blog
from post.models import Post, POSTED
from post.permissions import PostPermission
from post.serializers import PostListSerializer, PostCreateSerializer, PostSerializerWithoutBlog
from post.views import PostQueryset
from rest_framework import status
from rest_framework.filters import SearchFilter, OrderingFilter

from rest_framework.generics import RetrieveUpdateDestroyAPIView, GenericAPIView
from rest_framework.response import Response


class PostListAPI(PostQueryset, RetrieveUpdateDestroyAPIView):
    permission_classes = (PostPermission,)
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('title','summary')
    ordering_fields = ('title','posted_date')
    serializer_class = PostListSerializer

    def get(self, request, pk):
        blog = Blog.objects.filter(pk=pk)
        posts = Post.objects.filter(blog=blog)
        listaPost = []
        for post in posts:
            if request.user.is_superuser or request.user == post.blog.owner:  # compruebo si el usuario autenticado puede hacer GET en estos post
                listaPost.append(post)
            else:
                if post.visibility == POSTED:
                    listaPost.append(post)

        serializer = PostListSerializer(listaPost, many=True)
        return Response(serializer.data)


class PostDetailAPI(PostQueryset, RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializerWithoutBlog
    permission_classes = (PostPermission,)

    def get_queryset(self):
        return self.get_post_queryset(self.request)



class PostCreateAPI(GenericAPIView):
    permission_classes = (PostPermission,)
    serializer_class = PostCreateSerializer

    def post(self, request):
        post_with_owner = Post()
        self.check_permissions(request)  # compruebo si el usuario autenticado puede hacer POST
        blog = Blog.objects.filter(owner=request.user).all()
        post_with_owner.blog = blog[0]
        post_with_owner.owner = request.user  # asigno como propietario de la foto, el usuario autenticado
        post_with_owner.visibility = POSTED
        serializer = PostCreateSerializer(instance=post_with_owner, data=request.data)
        if serializer.is_valid():
            serializer.save()  # Guarda el objeto Photo y me lo devuelve
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
