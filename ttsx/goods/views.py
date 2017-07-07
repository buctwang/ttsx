# -*- coding:utf-8 -*-
from django.shortcuts import render

# Create your views here.

def index(request):
    content = {'title':'首页'}
    return render(request, 'goods/index.html/', content)