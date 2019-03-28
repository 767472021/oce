# -*- coding: utf-8 -*-
from .models import Banner


def get_index_banners():
    """
    获取首页可展示轮播图集合
    :return:
    """
    return Banner.objects.filter(is_show=True).order_by('order_number')
