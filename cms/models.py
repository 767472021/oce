# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime
from uuslug import slugify
from DjangoUeditor.models import UEditorField


# Create your models here.


class Category(models.Model):
    """
    分类
    """
    name = models.CharField(unique=True, verbose_name=u'分类名称', blank=True,
                            max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    level = models.IntegerField(verbose_name=u'等级', default=0)
    sort = models.IntegerField(verbose_name=u'排序值', default=0)
    parent = models.ForeignKey('self', default=0, null=True, blank=True,
                               related_name='children', verbose_name=u'上级分类',
                               limit_choices_to={'is_abort': False,
                                                 'is_root': True})
    is_root = models.BooleanField(default=False, verbose_name=u'是否是一级分类')
    is_abort = models.BooleanField(default=False, verbose_name=u'是否删除')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        db_table = 'oce_category'
        verbose_name = u'分类'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        if self.parent:
            return '%s--%s' % (self.name, self.parent)
        return self.name


class Story(models.Model):
    """
    内容管理
    """
    STATUS_CHOICES = (
        (1, u"待编辑"),
        (2, u"待审核"),
        (3, u"发布"),
        (4, u"存档"),
    )
    title = models.CharField(unique=True, verbose_name=u'标题', max_length=255)
    cover = models.ImageField(verbose_name=u'内容封面',
                              upload_to='story/images/%Y/%m', null=True,
                              blank=True, )

    slug = models.SlugField(unique=True, max_length=255)
    content = UEditorField(verbose_name=u'内容	', height=300, width=750,
                           default=u'', blank=True,
                           imagePath="story/images/",
                           toolbars='besttome', filePath='story/files/')
    category = models.ForeignKey(Category, verbose_name=u'分类', null=True,
                                 blank=True,
                                 limit_choices_to={'is_abort': False})
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    created = models.DateTimeField(verbose_name=u'创建时间', auto_now_add=True,
                                   blank=True)
    modified = models.DateTimeField(verbose_name=u'修改时间', auto_now=True,
                                    blank=True, null=True)
    hits = models.IntegerField(verbose_name=u'浏览次数', default=0)
    is_show = models.BooleanField(default=True, verbose_name=u'是否显示')

    class Meta:
        db_table = 'oce_story'
        ordering = ['modified']
        verbose_name = u'内容管理'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Story, self).save(*args, **kwargs)
