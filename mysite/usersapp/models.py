from django.db import models

""""
用户名
密码
邮箱地址
性别       male female
创建时间
"""


# Create your models here.
class User(models.Model):
    gender = (
        ('male', '男'),
        ('female', '女')
    )

    # 将来我的用户名　　必须唯一
    name = models.CharField(max_length=50, verbose_name='用户名', unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(verbose_name='邮箱')
    sex = models.CharField(max_length=6, choices=gender)
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name
        # 按照时间倒叙排序
        ordering = ['-c_time']
