# -*- coding:utf-8 -*-
from django.shortcuts import render, redirect
from hashlib import sha1
from .models import UserInfo
from django.http import JsonResponse
import datetime


def is_login(func):
    def wrapper(request):
        try:
            uid = request.session['uid']
        except KeyError:
            return redirect('/user/login/')
        return func(request)
    return wrapper

# Create your views here.
# 返回注册页面
def register(request):
    content = {'title':'注册'}
    return render(request, 'df-user/register.html', content)


# 验证提交的注册信息并注册
def register_check(request):
    # 读取数据
    post = request.POST
    user_name = post.get('user_name')
    user_pwd = post.get('pwd')
    user_cpwd = post.get('cpwd')
    user_email = post.get('email')

    # 验证提交的信息是否合法
    user_num = UserInfo.objects.filter(uname = user_name).count()
    if user_num != 0:
        return redirect('/user/register/')

    # 加密密码
    s1 = sha1()
    s1.update(user_pwd)
    user_pwd_sha1 = s1.hexdigest()
    print(user_pwd_sha1)

    # 将用户注册信息存数据库
    user = UserInfo()
    user.uname = user_name
    user.upwd = user_pwd_sha1
    user.uemail = user_email
    user.save()

    return redirect('/user/login/')


# 处理js ajax请求验证用户是否已经存在
def check_user_name(request):
    user_name = request.GET.get('name')
    user_num = UserInfo.objects.filter(uname=user_name).count()
    if user_num != 0:
        return JsonResponse({'status': 'error'})


# 返回登陆页面视图函数
def login(request):
    content = {'title':'登陆'}
    user_name = request.COOKIES.get('uname')
    if user_name is None:
        content['uname'] = ''
    else:
        content['uname'] = user_name
    return render(request, 'df-user/login.html', content)


# 登陆验证视图函数
def login_check(request):
    content = {'title': '登陆'}
    # 获取post提交过来的用户名和密码
    post = request.POST
    user_name = post.get('username')
    user_pwd = post.get('pwd')
    uremember_pwd = post.get('remember_pwd')

    # 若出现用户名或密码错误通过上下文讲上次输入的用户名密码显示在客户网页
    content['upwd'] = user_pwd
    content['uname'] = user_name
    # print(user_name)
    # 查找数据库该用户是否存在
    user_exist = UserInfo.objects.filter(uname=user_name).count()
    if user_exist == 0:
        content['username'] = '用户名错误'

        return render(request, 'df-user/login.html', content)

    s1 = sha1()
    s1.update(user_pwd)
    pwd_sha1 = s1.hexdigest()

    userinfo = UserInfo.objects.get(uname=user_name)
    if pwd_sha1 != userinfo.upwd:
        content['password'] = '密码错误'

        return render(request, 'df-user/login.html', content)
    # 程序到达这一步表明用户名和密码正确，使用ｃｏｏｋｉｅ记住用户名;去掉勾选删除cookie

    response = redirect('/user/user_center_info/')
    if uremember_pwd == '1':
        response.set_cookie('uname',user_name, expires=datetime.datetime.now() + datetime.timedelta(days=14))
    else:
        response.set_cookie('uname', max_age=-1)
    # 记住登陆用户的id，使用session
    request.session['uid'] = userinfo.id
    request.session.set_expiry(120)
    return response


# 用户中心用户信息
@is_login
def user_center_info(request):
    content = {'title':'用户中心'}
    # 从session中拿到用户
    uid = request.session['uid']
    user = UserInfo.objects.get(id=uid)
    content['uname'] = user.uname
    content['uphone'] = user.uphone
    content['uaddress'] = user.uaddress
    return render(request, 'df-user/user_center_info.html', content)


# 用户中心订单管理
@is_login
def user_center_order(request):
    content = {'title':'用户中心'}
    return render(request, 'df-user/user_center_order.html', content)


# 用户中心地址管理
@is_login
def user_center_site(request):
    content = {'title':'用户中心'}
    uid = request.session.get("uid")
    user = UserInfo.objects.get(id=uid)
    # 提交用户信息表单
    if request.method == 'POST':
        # 获取提交的各项数据
        post = request.POST
        uid = request.session.get("uid")
        user = UserInfo.objects.get(id=uid)
        user.ureccept_name = post.get('reccept_name')
        user.uaddress = post.get('address', '')
        user.ucode = post.get('code')
        user.uphone = post.get('phone')

        user.save()
    content['ucode'] = user.ucode
    content['uaddress'] = user.uaddress
    content['uname'] = user.ureccept_name
    content['uphone'] = user.uphone
    return render(request, 'df-user/user_center_site.html', content)




