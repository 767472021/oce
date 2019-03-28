# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='\u8f6e\u64ad\u6807\u9898')),
                ('detail', models.TextField(default=b'', null=True, verbose_name='\u63cf\u8ff0', blank=True)),
                ('image', models.ImageField(upload_to=b'upload/banner/%Y/%m/%d', verbose_name='\u8f6e\u64ad\u56fe\u7247')),
                ('link', models.URLField(default=b'', null=True, verbose_name='\u94fe\u63a5', blank=True)),
                ('order_number', models.PositiveIntegerField(default=0, verbose_name='\u8f6e\u64ad\u987a\u5e8f')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
                ('is_show', models.BooleanField(default=True, verbose_name='\u662f\u5426\u663e\u793a')),
            ],
            options={
                'ordering': ['order_number'],
                'db_table': 'oce_banner',
                'verbose_name': '\u9996\u9875\u8f6e\u64ad\u56fe',
                'verbose_name_plural': '\u9996\u9875\u8f6e\u64ad\u56fe',
            },
        ),
    ]
