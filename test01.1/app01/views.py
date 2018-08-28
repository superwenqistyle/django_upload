from django.shortcuts import render
from .models import Publisher
from django.http import HttpResponse
import json
from django.forms import model_to_dict
# django框架带的序列化
# from django.core import serializers
from app01 import serializers


# Create your views here.
# 先用最古老的一种方式　给用户去返回　web api　
def publisher(request):
    # ORM的查询集
    queryset = Publisher.objects.all()

    # 第二次改进
    # data = serializers.serialize('json', queryset)

    # 第三次改进
    s = serializers.PublisherSerializer(queryset, many=True)

    return HttpResponse(json.dumps(s.data), content_type='application/json')

    # 列表　里面装的是　一个个字典
    # data = []
    # for i in queryset:
    #     # 第一次改进
    #     data.append(model_to_dict(i))
    #     # tmp = {
    #     #     'name': i.name,
    #     #     'address': i.address
    #     # }
    #     # data.append(tmp)
