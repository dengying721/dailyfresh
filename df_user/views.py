from django.http import JsonResponse
from django.shortcuts import render, redirect, HttpResponse
from .models import *
from hashlib import sha1


# Create your views here.
def register(request):
    return render(request, 'df_user/register.html')


def register_handle(request):
    print('---------------arrived register_handle...-----------------')
    post = request.POST
    uname = post.get('username')
    upwd = post.get('password')
    ucpwd = post.get('confirm')
    uemail = post.get('email')
    print('===============')
    print(uname)
    print('===============')

    # 判断两次密码是否一致
    if upwd != ucpwd:
        return redirect('/user/register')
    s1 = sha1()
    s1.update(upwd.encode('utf8'))
    upwd2 = s1.hexdigest()
    # 创建对象
    user = UserInfo()
    user.uname = uname
    user.upwd = upwd2
    user.uemail = uemail
    user.save()
    return redirect('/user/login')


def register_exist(request):
    uname = request.GET.get('uname')
    count = UserInfo.objects.filter(uname=uname).count()
    print('count is : %s' % count)
    return JsonResponse({'count': count})


def login(request):
    return render(request, 'df_user/login.html')


def login_handle(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    return HttpResponse("hello, waiting to deal...")


def user_exit(request):
    name = request.GET.get('uname')
    print('登录时候的用户名检查的是：%s' % name)
    print(UserInfo.objects.filter(uname=name).exists())
    return HttpResponse({'is_exist':UserInfo.objects.filter(uname=name).exists()})


def find_password(request):
    return HttpResponse("hello, boy , find your password ? no way!")
