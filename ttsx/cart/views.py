# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import JsonResponse
from models import CartInfo
from df_user.models import UserInfo
from df_user import user_decoration


# Create your views here.
# 箱购物车中增加一个商品
def add(request):
    gid = request.GET.get('gid')
    uid = request.session.get('uid')
    gnum = int(request.GET.get('gnum', 1))

    # 如果该用户已经已经添加过该商品，只把数量增长，否则创建一条新的记录
    cartinfo = CartInfo.objects.filter(user_id=uid, goods_id=gid)
    count = cartinfo.count()
    if count == 0:
        cart = CartInfo()
        cart.goods_id = gid
        cart.user_id = uid
        cart.num = gnum
    else:
        cart = cartinfo[0]
        cart.num += gnum;
    cart.save()
    return JsonResponse({'success':1})


# 查询购物车中存在几类商品
def count(request):
    uid = request.session.get('uid')
    count = CartInfo.objects.filter(user_id=uid).count()
    return JsonResponse({'count':count})


# 显示购物车页面
@user_decoration.is_login
def cart(request):
    content={'title':'购物车'}
    uid = request.session.get('uid')
    glist = CartInfo.objects.filter(user_id=uid)
    content['glist'] = glist
    return render(request, 'cart/cart.html', content)