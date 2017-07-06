# -*- coding:utf-8 -*-
from django.db import models

# Create your models here.
# 用户信息模型类
class UserInfo(models.Model):
    uname = models.CharField(max_length=20)
    upwd = models.CharField(max_length=40)
    uemail = models.CharField(max_length=40)
    uaddress = models.CharField(max_length=100, default='')
    ureccept_name = models.CharField(max_length=20,default='')
    ucode = models.CharField(max_length=6, default='')
    uphone = models.CharField(max_length=11, default='')
