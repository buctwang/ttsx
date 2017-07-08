# -*- coding:utf-8 -*-
from django.shortcuts import render
from .models import GoodsInfo, GoodsType
from django.core.paginator import Paginator


# 查询所有商品类别
def all_type():
    types = GoodsType.objects.all()
    return types


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
    good = GoodsInfo.objects.get(pk=gid)
    # 增加一次点击量，保存数据库，在列表页可以按点击量排序
    good.click += 1
    good.save()
    # 查询最新的两个商品
    new_goods = good.type.goodsinfo_set.order_by('-id')[0:2]
    content['new_goods'] = new_goods
    content['good'] = good
    return render(request, 'goods/detail.html', content)


# 显示商品列表页
def list(request, tid, page_index):
    content = {'title': '商品列表', 'search_style': '1'}
    # 商品排序依据 1默认　２价格　３人气
    order_by = request.GET.get('order_by')
    content['order_by'] = order_by

    # 查询相应的商品类别
    type = GoodsType.objects.get(pk=int(tid))
    content['type'] = type
    # 查询该类别下的所有商品
    if order_by == '1':
        goods = type.goodsinfo_set.order_by('id')
    elif order_by == '2':
        goods = type.goodsinfo_set.order_by('price')
    else:
        goods = type.goodsinfo_set.order_by('-click')
    # 新品推荐的两个商品
    new_goods = GoodsInfo.objects.filter(type=type).order_by('-id')[0:2]
    content['new_goods'] = new_goods

    # 分页
    paginator = Paginator(goods, 15)
    page = paginator.page(int(page_index))
    content['page'] = page
    return render(request, 'goods/list.html/', content)

