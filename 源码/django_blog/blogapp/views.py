from django.shortcuts import render
from .models import Banner, Post, FriendlyLink, BlogCategory, Comment
from django.views.generic.base import View
from django.db.models import Q


# 基于类的视图
class SearchView(View):

    # post  get
    def post(self, request):
        # 如果要搜索的话  前段必然是要传一个关键字进来
        # 　根据这个关键字　去　　数据库里面查找
        kw = request.POST.get('keyword')
        # 拿到这个keyword就要　　去数据库里面找

        #  你要找什么　　　找博客名字＋博客内容
        # Q
        post_list = Post.objects.filter(Q(title__contains=kw) | Q(content__contains=kw))

        ctx = {
            'post_list': post_list
        }

        return render(request,'search_list.html',ctx)


def blog_list(request):
    return render(request, 'search_list.html')


# 基于函数的视图
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

    # 取出博客分类里面的数据
    categary_list = BlogCategory.objects.all()

    new_comment_list = Post.objects.filter(comment__content__isnull=False).order_by('-pub_date')

    ctx = {
        'banner_list': banner_list,
        'recomment_list': recomment_list,
        'post_list': post_list,
        'friend_list': friend_link,
        'categary_list': categary_list,
        'new_comment_list': new_comment_list
    }

    return render(request, 'index.html', ctx)
