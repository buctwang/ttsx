# -*- coding:utf-8 -*-
from django.db import models
from tinymce.models import HTMLField


# Create your models here.
class GoodsType(models.Model):
    type = models.CharField(max_length=20)
    isdelete = models.BooleanField(default=False)


class GoodsInfo(models.Model):
    title = models.CharField(max_length=20)
    pic = models.ImageField(upload_to='goods/')
    price = models.DecimalField(max_digits=5, decimal_places=2)
    click = models.IntegerField()   # 点击量
    unit = models.CharField(max_length=10)  # 单位
    isDelete = models.BooleanField(default=False)
    subtitle = models.CharField(max_length=200)  # 商品详情页副标题
    store = models.IntegerField(default=100)  # 库存
    content = HTMLField()  # 商品详情页商品介绍
    type = models.ForeignKey('GoodsType')

