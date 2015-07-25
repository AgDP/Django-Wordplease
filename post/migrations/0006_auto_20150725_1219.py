# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_auto_20150725_1218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='visibility',
            field=models.CharField(default=b'PRI', max_length=3, choices=[(b'PUB', b'Publicado'), (b'PRI', b'Pendiente Publicar')]),
        ),
    ]
