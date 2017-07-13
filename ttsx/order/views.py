# -*- coding:utf-8 -*-
from django.shortcuts import render
from cart.models import CartInfo
from df_user.models import UserInfo
from django.db import transaction

# Create your views here.


def order(request):
    content = {'title':'提交订单'}
    uid = request.session.get('uid')
    user = UserInfo.objects.get(id=uid)
    content['user'] = user
    cart_id = request.POST.getlist('cart_id')
    cart_list = CartInfo.objects.filter(id__in=cart_id)
    content['cart_list'] = cart_list
    return render(request, 'order/place_order.html/', content)


@transaction.atomic
def commit(request):
    pass