# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import Category, Story
from .utils import get_format_datetime


class StorySerializer(serializers.ModelSerializer):
    created = serializers.SerializerMethodField()

    def get_created(self, obj):
        return get_format_datetime(obj.created)

    class Meta:
        model = Story
        fields = '__all__'
