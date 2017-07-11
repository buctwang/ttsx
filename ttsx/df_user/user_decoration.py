# -*- coding:utf-8 -*-
from django.shortcuts import redirect


# 判断是否登陆，若登陆执行后续函数，未登录则转向登陆页面
def is_login(func):
    def wrapper(request, *args, **kwargs):
        try:
            uid = request.session['uid']
        except KeyError:
            return redirect('/user/login/')
        return func(request, *args, **kwargs)
    return wrapper
