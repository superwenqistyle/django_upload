from django.shortcuts import render, redirect, reverse
from .models import Banner, Post, FriendlyLink, BlogCategory, Comment, Tags
from userapp.models import BlogUser
from django.views.generic.base import View
from django.db.models import Q
# 导入第三方分页的组件
from pure_pagination import Paginator, PageNotAnInteger


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

        return render(request, 'search_list.html', ctx)


# 列表页面　　　　　
def blog_list(request):
    # 找出所有的博客　展示出来
    post_list = Post.objects.all().order_by('-pub_date')

    # 找出虽所有的标签
    tags_list = Tags.objects.all()

    # 获取最新文章列表
    new_comment_list = Post.objects.filter(comment__content__isnull=False).order_by('-pub_date')

    # 去重
    new_comment_list2 = []

    for blog in new_comment_list:
        if blog in new_comment_list2:
            pass
        else:
            new_comment_list2.append(blog)

    # 分页

    # try:
    #     page = request.GET.get('page', 1)
    # except PageNotAnInteger:
    #     page = 1
    # p = Paginator(post_list, per_page=1, request=request)
    # post_list = p.page(page)

    ctx = {
        'post_list': post_list,
        'tags_list': tags_list,
        'new_comment_list': new_comment_list2
    }

    return render(request, 'list.html', ctx)


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

    # 这个功能是　返回最新的评论列表
    new_comment_list = Post.objects.filter(comment__content__isnull=False).order_by('-pub_date')

    # 空列表　
    new_comment_list2 = []

    # 所有博客的总数
    count = post_list.count()

    for blog in new_comment_list:
        if blog in new_comment_list2:
            pass
        else:
            new_comment_list2.append(blog)

    ctx = {
        'banner_list': banner_list,
        'recomment_list': recomment_list,
        'post_list': post_list,
        'friend_list': friend_link,
        'categary_list': categary_list,
        'new_comment_list': new_comment_list2,
        'count': count
    }

    return render(request, 'index.html', ctx)


# 当我们跳转详情页面的时候　　我们要知道　我们到低　跳的是哪一篇?
def show(request, page):
    page = int(page)
    # 获取指定id的文章　
    # 这个id当时我们在配置url的时候　　写了一个正则表达式　　来匹配这个id
    blog = Post.objects.get(id=page)

    # show这个详情页面的ＵＲＬ每调一次　　是不是就执行一次我们这个show函数
    blog.views += 1
    # 保存
    blog.save()

    # 相关推荐
    # 我去查询我的数据库,只要,数据库里面其他的博客　或者其他博客里面的内容有我当前这个博客里面的标题

    recomment_list = Post.objects.filter(Q(title__contains=blog.title) | Q(content__contains=blog.title))

    # 获取最新评论文章
    new_comment_list = Post.objects.filter(comment__isnull=False).order_by('-pub_date')

    new_comment_list2 = []
    # 去重
    for blog in new_comment_list:
        if blog in new_comment_list2:
            pass
        else:
            new_comment_list2.append(blog)

    ctx = {
        'blog': blog,
        'recomment_list': recomment_list,
        'new_comment_list': new_comment_list2
    }

    return render(request, 'show.html', ctx)


def comment_handle(request):
    # 取到的就是那篇博客的id
    blog_id = request.POST.get('blog_id')

    # 取前端传过来的　　用户名
    username = request.POST.get('username')
    # 取前端传过来的邮箱
    email = request.POST.get('email')
    # 取前端传过来的　　评论内容
    comment = request.POST.get('comment-text')

    # 实例化一个评论模型
    c = Comment()
    # 评论模型里面有一个user字段　是必须要填
    c.user = BlogUser.objects.get(id=1)
    # 评论的内容
    c.content = comment
    # 还需要提交博客的id 因为　我们要知道这个评论属于哪个博客下面的评论
    c.post = Post.objects.get(id=blog_id)
    c.save()

    return redirect(reverse('blogapp:show', args=(blog_id,)))
