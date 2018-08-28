from .models import Publisher
from app01 import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from rest_framework import generics, mixins


# 第三次改进
# 查询所有　　创建新的　出版社
# class PublisherList(mixins.CreateModelMixin,
#                     mixins.ListModelMixin,
#                     generics):
#     queryset = Publisher.objects.all()
#     serializers_class = serializers.PublisherSerializers
#


# class PublisherList(APIView):
#     # get请求
#     def get(self, request, format=None):
#         queryset = Publisher.objects.all()  # 获取所有的出版社信息
#         s = serializers.PublisherSerializers(queryset, many=True)
#         return Response(s.data, status=status.HTTP_200_OK)
#
#     # post请求
#     def post(self, request, format=None):
#         s = serializers.PublisherSerializers(data=request.data)
#         if s.is_valid():
#             s.save()
#             return Response(s.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class PublisherDetail(APIView):
#     # 这个类　查询　更新　　删除某个具体的　出版社　
#     def get_object(self, pk):
#         # publisher = Publisher.objects.get(id=pk)
#         try:
#             publisher = Publisher.objects.get(id=pk)
#             return publisher
#         except Publisher.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#
#     def get(self, request, pk):
#         s = serializers.PublisherSerializers(self.get_object(pk))
#         return Response(s.data, status=status.HTTP_200_OK)
#
#     def put(self, request, pk):
#         s = serializers.PublisherSerializers(self.get_object(pk), request.data)
#         if s.is_valid():
#             s.save()
#             return Response(s.data, status=status.HTTP_200_OK)
#         else:
#             return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self,request,pk):
#         self.get_object(pk).delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET', 'POST'])
# def publisher_list(request):
#     if request.method == 'GET':
#         # 要想罗列出所有的
#         queryset = Publisher.objects.all()
#         s = serializers.PublisherSerializers(queryset, many=True)
#         return Response(s.data, status=status.HTTP_200_OK)
#     elif request.method == 'POST':
#         # 将用户　传过来的　数据进行序列化
#         s = serializers.PublisherSerializers(data=request.data)
#         if s.is_valid():  # 验证序列化后的数据是否符合规定
#             s.save()  # 保存到数据库
#             return Response(s.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(s.errors, status=status.HTTP_404_NOT_FOUND)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def publisher_detail(request, pk):
#     try:
#         # publisher对象　存的就是出版社信息　本质　　数据库里面　pk指定的那一条数据
#         queryset = Publisher.objects.get(id=pk)  # 如果找不到pk对应的整条数据
#     except Publisher.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         s = serializers.PublisherSerializers(queryset)
#         return Response(s.data, status=status.HTTP_200_OK)
#
#     if request.method == 'PUT':
#         s = serializers.PublisherSerializers(queryset, data=request.data)
#         # 判断校验
#         if s.is_valid():
#             s.save()
#             return Response(s.data, status=status.HTTP_200_OK)
#         else:
#             return Response(s.data, status=status.HTTP_400_BAD_REQUEST)
#
#     if request.method == 'DELETE':
#         queryset.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# ---------------------------------------------------------------
# from django.core import serializers

# Create your views here.
# def publisher(request):
#     # 我们要从数据库里面取出所有的出版社信息
#     # queryset 是一个列表　列表里面装了一个个对象　每一个对象就是数据库里面的一行数据
#     queryset = Publisher.objects.all()
#
#     # 第二次改进
#     # data = serializers.serialize('json', queryset)
#
#     # 第三次改进 DRF
#     # many=True----> 告诉　
#     s = serializers.PublisherSerializers(queryset, many=True)
#
#     return HttpResponse(json.dumps(s.data), content_type='application/json')
#
#     # 第一次改进 图片　
#     # data = []
#     # for i in  queryset:
#     #     data.append(model_to_dict(i))
#     # return  HttpResponse(json.dumps(data),content_type='application/json')
#     #
#
#     # # 老办法--->手动的去写映射关系
#     # data = []
#     # # 遍历
#     # for i in queryset:
#     #     # 创建一个字典
#     #     tmp = {
#     #         'name': i.name,
#     #         'address': i.address
#     #     }
#     #     data.append(tmp)
#     # return HttpResponse(json.dumps(data), content_type='application/json')
