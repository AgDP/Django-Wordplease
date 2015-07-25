# -*- coding: utf-8 -*-
from blog.models import Blog
from category.models import Category
from django.db import models

POSTED = 'PUB'
NOTPOSTED = 'PRI'

VISIBILITY = (
    (POSTED, 'Publicado'),
    (NOTPOSTED, 'Pendiente Publicar')
)

class Post(models.Model):

    blog = models.ForeignKey(Blog)
    title = models.CharField(max_length=150)
    summary = models.CharField(max_length=500)
    body = models.CharField(max_length=1000)
    url = models.URLField(blank=True)
    posted_date = models.DateTimeField(auto_now=True)
    category = models.ManyToManyField(Category, blank=True)
    visibility = models.CharField(max_length=3, choices=VISIBILITY, default=NOTPOSTED)

    def __unicode__(self):  # 0 param method
        return self.title