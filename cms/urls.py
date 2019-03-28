# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from .views import CmsList, CmsDetail, SearchView

urlpatterns = [
    url(r'^search/$', SearchView, name="cms-search"),
    url(r'^cms/$', CmsList.as_view(), name="cms"),
    url(r'^cms_detail/', CmsDetail.as_view(), name="cms_detail"),
]
