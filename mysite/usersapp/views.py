from django.shortcuts import render, redirect
from usersapp.models import User
from .forms import UserForm


# Create your views here.
def login(request):
    if request.method == 'POST':

        login_forms = UserForm(request.POST)

        message = ''
        # 用户提交表单的时候　才会进到这个if
        # username = request.POST.get('username', None)
        # password = request.POST.get('password', None)

        # 先确定　　有没有账号和密码
        # is_valid()  符合规律的数据　TRUE
        if login_forms.is_valid():
            # 取出　用户名
            username = login_forms.cleaned_data['username']
            # 取出密码
            password = login_forms.cleaned_data['password']

            # 处理了我的用户名
            username = username.strip()
            # 有了用户名以后　　先找账号　如果账号存在　比较密码
            # 如果账号不存在　　
            try:
                # 去数据库里面找到　　用户前端输入过来的这个用户
                user = User.objects.get(name=username)
                if user.password == password:
                    return redirect('/index/')
                else:
                    message = '密码错误'
                    return render(request, 'login.html', locals())
            except:
                message = '该用户不存在'
                return render(request, 'login.html', locals())

        return redirect('/index/')

    else:
        login_forms = UserForm()
        # 通过浏览器地址栏输入进来的get请求
        return render(request, 'login.html', locals())


def register(request):
    return render(request, 'register.html')


def logout(request):
    return redirect('/index/')


def index(request):
    return render(request, 'index.html')
