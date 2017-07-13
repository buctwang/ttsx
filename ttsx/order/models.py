# -*-coding:utf-8-*-
from django.db import models
from df_user.models import UserInfo
from goods.models import GoodsInfo


# Create your models here.
class OrderMain(models.Model):
    orderid = models.CharField(max_length=20, primary_key=True)
    user = models.ForeignKey(UserInfo)
    time = models.DateTimeField(auto_now_add=True)
    count = models.DecimalField(max_digits=8, decimal_places=2) # 总价


class OrderDetail(models.Model):
    order = models.ForeignKey(OrderMain)
    goods = models.ForeignKey(GoodsInfo)
    num = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
