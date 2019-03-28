# -*- coding: utf-8 -*-
from django.contrib import admin
from cms.models import Category, Story


class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ['slug']
    list_display = ('name', 'parent', 'level', 'sort', 'is_root', 'is_abort')


class StoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created', 'modified', 'category', 'is_show')
    search_fields = ('title', 'content')
    list_filter = ('status', 'created', 'modified')
    readonly_fields = ['slug']

admin.site.register(Story, StoryAdmin)

admin.site.register(Category, CategoryAdmin)
