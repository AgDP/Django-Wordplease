# -*- coding: utf-8 -*-
from rest_framework import serializers
from models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        #read_only_fields = ('blog',)


class PostSerializerWithoutBlog(serializers.ModelSerializer):
    class Meta:
        model = Post
        read_only_fields = ('blog',)

class PostListSerializer(PostSerializer):

    class Meta(PostSerializer.Meta):
        fields = ('title', 'summary', 'url', 'posted_date')

class PostCreateSerializer(PostSerializer):

    id = serializers.ReadOnlyField()  # read only
    blog = serializers.CharField()
    title = serializers.CharField()
    summary = serializers.CharField()
    body = serializers.CharField()
    url = serializers.CharField()
    #posted_date = serializers.DateTimeField()
    category = serializers.CharField()
    #visibility = serializers.CharField()

    def create(self, validated_data):

        instance = Post()
        return self.update(instance, validated_data)

    def update(self, instance, validated_data):

        #instance.blog = validated_data.get('blog')
        instance.title = validated_data.get('title')
        instance.summary = validated_data.get('summary')
        instance.body = validated_data.get('body')
        instance.url = validated_data.get('url')
        #instance.category = validated_data.get('category')
        #instance.visibility = validated_data.get('visibility')
        instance.save()
        return instance