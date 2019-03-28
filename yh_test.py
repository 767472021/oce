# -*- coding: utf-8 -*-

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web.settings")  # NoQA
import django

django.setup()

from cms.models import Story
from django.db.models import Q

x = Story.objects.filter(Q(category__name='新闻中心') | Q(
    category__parent__name='新闻中心')).filter(status=3).order_by('-created')
print len(x)
print x[2].created, x[0].title

CMS_MAP = {
    "xin-wen-zhong-xin": "新闻中心",
    "chan-pin-zhong-xin": "产品中心"
}

x = CMS_MAP.values()
print x
