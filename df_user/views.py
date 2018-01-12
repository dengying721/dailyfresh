from django.http import JsonResponse, HttpResponseRedirect
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
    uname = request.COOKIES.get('uname', '')
    context = {'title': '用户登录', 'error_name':0, "error_pwd": 0, 'uname': uname}
    return render(request, 'df_user/login.html', context)


# 登录请求处理
def login_handle(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    is_remember = request.POST.get('jizhu')
    print("name is : %s" % username)
    print("password is : %s" % password)

    users = UserInfo.objects.filter(uname=username)
    print(users)
    if len(users) == 1:
        s1 = sha1()
        s1.update(password.encode('utf-8'))
        s_pwd = s1.hexdigest()
        upwd = users[0].upwd

        if s_pwd == upwd:
            red = HttpResponseRedirect('/user/info')
            if is_remember != 0:
                print('---------------------the remember is 1.')
                red.set_cookie('uname', username)
            else:
                print('----------------------the remember is 0.')
                red.set_cookie('uname', '', max_age=-1)
            return red
        else:
            context = {'title': '用户登录1', 'error_name': 0, 'error_pwd': 1, 'uname': username, 'upwd': password}
            print("enter else ...")
            return render(request, 'df_user/login.html', context)
    else:
        context = {'title': '用户登录2', 'error_name': 1, 'error_pwd': 0, 'uname': username, 'upwd': password}
        return render(request, 'df_user/login.html', context)


#登录时判断用户名是否存在
def user_exit(request):
    name = request.GET.get('uname')
    print('登录时候的用户名检查的是：%s' % name)
    print("该用户是否存在：%s" % UserInfo.objects.filter(uname=name).exists())
    return JsonResponse({'is_exist':UserInfo.objects.filter(uname=name).exists()})


def find_password(request):
    return HttpResponse("hello, boy , find your password ? no way!")


def login_index(request):
    return HttpResponse("hello , index!")


def user_info(request):
    return render(request, 'df_user/user_center_info.html')
