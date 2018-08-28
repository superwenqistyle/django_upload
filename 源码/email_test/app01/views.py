from django.shortcuts import render
# 导入settingｓ文件
from django.conf import settings
# 　导入发邮件的模块
from django.core.mail import send_mail
from django.http import HttpResponse
from random import Random

# 生成一个随机数的函数　a-z A-Z 0-9
# 生成随机字符串
def make_random_str(randomlength=8):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str+=chars[random.randint(0, length)]
    return str

# Create your views here.
def send(request):
    # 这是要发送的　ＨＴＭＬ内容
    msg = '<a href="http://127.0.0.1:8000/yanzhen/{}/" target="_blank">点击激活</a>'.format(make_random_str(10))
    # 发送的函数
    send_mail('注册激活', '', settings.EMAIL_FROM,
              ['django_eamil_test@163.com'],
              html_message=msg)
    return HttpResponse('发送成功')

def yanzhen(request,a):

    print(a)
    return HttpResponse('验证成功')