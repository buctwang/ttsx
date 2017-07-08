# -*- coding:utf-8 -*-
from django.shortcuts import render
from .models import GoodsInfo, GoodsType


# Create your views here.
# 显示首页
def index(request):
    content = {'title':'首页', 'search_style':'1'}
    # 页面显示图片商品为最新的商品，商品类别右边为最热（点击量）商品，分别从数据库中排序筛选
    goodstype = GoodsType.objects.all()
    list = []
    for temp in goodstype:
        new_list = temp.goodsinfo_set.order_by('-id')[0:4]
        hot_list = temp.goodsinfo_set.order_by('-click')[0:4]
        goods = {'new_list':new_list, 'hot_list':hot_list, 'goodstype':temp}
        list.append(goods)
    content['list'] = list
    return render(request, 'goods/index.html/', content)


# 显示详情页
def detail(request, gid):
    content = {'title':'商品详情', 'search_style':'1'}
    good = GoodsInfo.objects.get(id=gid)
    content['good'] = good
    return render(request, 'goods/detail.html', content)