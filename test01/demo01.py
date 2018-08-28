# -*- coding: utf-8 -*-
# @Time    : 18-8-27 上午10:52
# @Author  : wengwenyu
# @Email   : wengwenyu@aliyun.com
# @File    : demo01.py
# @Software: PyCharm
import json

d = {'name': 'zhangsan', 'age': 18}
print(type(d))
# 把一个字典　序列化成一个　json字符串对象
json_str = json.dumps(d)
print(type(json_str))
# 别人给我们一个json字符串　　
d2 = json.loads(json_str)
print(type(d2))