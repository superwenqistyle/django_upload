# -*- coding: utf-8 -*-
# @Time    : 18-8-27 上午9:43
# @Author  : wengwenyu
# @Email   : wengwenyu@aliyun.com
# @File    : serializers.py
# @Software: PyCharm

from rest_framework import serializers
from .models import Publisher


# 第四次改进
class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        # 我们要序列化的模型
        model = Publisher
        # 我们要序列化的字段
        fields = (
            'id',
            'name',
            'address',

        )


# class PublisherSerializer(serializers.Serializer):
#     # 只读操作
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(max_length=32)
#     address = serializers.CharField(max_length=128)
#
#     def create(self, validated_data):
#         """
#         Create and return a new `Snippet` instance, given the validated data.
#         """
#         return Publisher.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Snippet` instance, given the validated data.
#         """
#         instance.name = validated_data.get('name', instance.title)
#         instance.address = validated_data.get('address', instance.code)
#         instance.save()
#         return instance
