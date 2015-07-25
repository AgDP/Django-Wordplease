# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models

class Blog(models.Model):

    owner = models.ForeignKey(User)
    title = models.CharField(max_length=100)

    def __unicode__(self):  # 0 param method
        return self.title