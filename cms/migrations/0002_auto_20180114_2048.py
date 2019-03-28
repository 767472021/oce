# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(unique=True, max_length=255, verbose_name='\u5206\u7c7b\u540d\u79f0', blank=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(unique=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='story',
            name='slug',
            field=models.SlugField(unique=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='story',
            name='title',
            field=models.CharField(unique=True, max_length=255, verbose_name='\u6807\u9898'),
        ),
    ]
