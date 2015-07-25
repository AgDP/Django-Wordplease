# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_post_visibility'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='visibility',
            field=models.CharField(default=b'NOP', max_length=3, choices=[(b'POS', b'Publicado'), (b'NOP', b'Pendiente Publicar')]),
        ),
    ]
