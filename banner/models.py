# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime

# Create your models here.


class Banner(models.Model):
    """
    首页轮播图
    """
    title = models.CharField(verbose_name=u'轮播标题', max_length=255)
    detail = models.TextField(verbose_name=u'描述', null=True, blank=True, default='')
    image = models.ImageField(verbose_name=u'轮播图片', upload_to='upload/banner/%Y/%m/%d')
    link = models.URLField(verbose_name=u'链接', null=True, blank=True, default='')
    order_number = models.PositiveIntegerField(
        verbose_name=u'轮播顺序', null=False, blank=False, default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    updated = models.DateTimeField(auto_now=True, verbose_name=u'更新时间')
    is_show = models.BooleanField(default=True, verbose_name=u'是否显示')

    class Meta:
        db_table = 'oce_banner'
        ordering = ["order_number"]
        verbose_name = u'首页轮播图'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return u'%s-%s' % (self.order_number, self.title)