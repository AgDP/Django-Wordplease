# -*- coding: utf-8 -*-
from django.db import models


class Category(models.Model):

    name = models.CharField(max_length=150)

    def __unicode__(self):  # 0 param method
        return self.name