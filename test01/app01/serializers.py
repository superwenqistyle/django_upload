# -*- coding: utf-8 -*-
# @Time    : 18-8-27 上午11:26
# @Author  : wengwenyu
# @Email   : wengwenyu@aliyun.com
# @File    : serializers.py
# @Software: PyCharm
# 导入DRF里面的serializers模块
from rest_framework import serializers
from . import models


class PublisherSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Publisher
        fields = ('id', 'name', 'address')

# # 模型名＋Serializers
# class PublisherSerializers(serializers.Serializer):
#     # 因为在模型里面　id是一个主键　　所以我们在序列化的时候
#     # 要特别小心　不能去修改主键
#     id = serializers.CharField(read_only=True)
#     name = serializers.CharField(max_length=32)
#     address = serializers.CharField(max_length=128)
#
#     def create(self, validated_data):
#         """
#         Create and return a new `Snippet` instance, given the validated data.
#         """
#         return models.Publisher.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Snippet` instance, given the validated data.
#         """
#         instance.name = validated_data.get('name', instance.name)
#         instance.address = validated_data.get('address', instance.address)
#
#         instance.save()
#         return instance
