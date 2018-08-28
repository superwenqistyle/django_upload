from django.shortcuts import render
from .models import Banner, Post,FriendlyLink


# Create your views here.
def index(request):
    # 取出所有的幻灯片
    banner_list = Banner.objects.all()
    # 取出所有被推荐的博客
    recomment_list = Post.objects.filter(recommend=True)
    # 取出所有博客  按照时间倒叙排列
    post_list = Post.objects.order_by('-pub_date').all()

    # 取出友情链接
    friend_link = FriendlyLink.objects.all()


    ctx = {
        'banner_list': banner_list,
        'recomment_list': recomment_list,
        'post_list': post_list,
        'friend_list':friend_link
    }

    return render(request, 'index.html', ctx)
