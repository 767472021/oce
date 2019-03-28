# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import DjangoUeditor.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50, verbose_name='\u5206\u7c7b\u540d\u79f0', blank=True)),
                ('slug', models.SlugField(unique=True)),
                ('level', models.IntegerField(default=0, verbose_name='\u7b49\u7ea7')),
                ('sort', models.IntegerField(default=0, verbose_name='\u6392\u5e8f\u503c')),
                ('is_root', models.BooleanField(default=False, verbose_name='\u662f\u5426\u662f\u4e00\u7ea7\u5206\u7c7b')),
                ('is_abort', models.BooleanField(default=False, verbose_name='\u662f\u5426\u5220\u9664')),
                ('parent', models.ForeignKey(related_name='children', default=0, blank=True, to='cms.Category', null=True, verbose_name='\u4e0a\u7ea7\u5206\u7c7b')),
            ],
            options={
                'db_table': 'oce_category',
                'verbose_name': '\u5206\u7c7b',
                'verbose_name_plural': '\u5206\u7c7b',
            },
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name='\u6807\u9898')),
                ('slug', models.SlugField(unique=True)),
                ('content', DjangoUeditor.models.UEditorField(default='', verbose_name='\u5185\u5bb9\t', blank=True)),
                ('status', models.IntegerField(default=1, choices=[(1, '\u5f85\u7f16\u8f91'), (2, '\u5f85\u5ba1\u6838'), (3, '\u53d1\u5e03'), (4, '\u5b58\u6863')])),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='\u4fee\u6539\u65f6\u95f4', null=True)),
                ('hits', models.IntegerField(default=0, verbose_name='\u6d4f\u89c8\u6b21\u6570')),
                ('is_show', models.BooleanField(default=True, verbose_name='\u662f\u5426\u663e\u793a')),
                ('category', models.ForeignKey(verbose_name='\u5206\u7c7b', blank=True, to='cms.Category', null=True)),
            ],
            options={
                'ordering': ['modified'],
                'db_table': 'oce_story',
                'verbose_name': '\u5185\u5bb9\u7ba1\u7406',
                'verbose_name_plural': '\u5185\u5bb9\u7ba1\u7406',
            },
        ),
    ]
