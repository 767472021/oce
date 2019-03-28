# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0002_auto_20180114_2048'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='cover',
            field=models.ImageField(upload_to=b'story/images/%Y/%m', null=True, verbose_name='\u5185\u5bb9\u5c01\u9762', blank=True),
        ),
    ]
