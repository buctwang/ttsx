from django.db import models


# Create your models here.
class CartInfo(models.Model):
    goods = models.ForeignKey('goods.GoodsInfo')
    user = models.ForeignKey('df_user.UserInfo')
    num = models.IntegerField(default=1)
