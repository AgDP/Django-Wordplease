# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
        ('post', '0002_auto_20150720_1905'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='owner',
        ),
        migrations.AddField(
            model_name='post',
            name='blog',
            field=models.ForeignKey(default=1, to='blog.Blog'),
            preserve_default=False,
        ),
    ]
