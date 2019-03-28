# -*- coding: utf-8 -*-
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Story
from django.db.models import Q


def get_format_datetime(datetime_arg):
    if not datetime_arg:
        return ''
    return datetime_arg.strftime('%Y-%m-%d')


def paginate(data, current_page=1, page_num=4):
    """
    分页函数
    """
    paginator = Paginator(data, page_num)
    try:
        show_lines = paginator.page(current_page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        show_lines = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        show_lines = paginator.page(paginator.num_pages)
    return show_lines


def list_url_by_args(url_base, **kwargs):
    params = kwargs.items()
    params.sort()
    get_params = [u'='.join([u'%s' % k, u'%s' % v]) for k, v in params if v]
    if get_params:
        return u'%s?%s' % (url_base, u'&'.join(get_params))
    else:
        return url_base


def get_obj4fso_cms(action, args):
    if action == 'index_view':
        objs = Story.objects.filter(Q(category__name=args) | Q(
            category__parent__name=args)).filter(status=3).order_by(
            '-created')[:3]
        return objs
    elif action == 'search':
        story_list = Story.objects.filter(
            Q(title__contains=args) | Q(content__contains=args))
        return story_list
    cms_obj = Story.objects.filter(Q(category__name=args) | Q(
        category__parent__name=args)).filter(status=3).order_by(
        '-created')
    return cms_obj


def get_slug4fso_cms(args):
    obj = Story.objects.filter(
        category__name=args,
    ).first()
    if obj:
        return obj.category.slug
    return None
