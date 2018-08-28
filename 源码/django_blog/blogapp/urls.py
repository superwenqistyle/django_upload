from django.conf.urls import url
from blogapp import views

urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^search/$', views.SearchView.as_view(), name='search'),
    url(r'^blog_list/$', views.blog_list, name='blog_list')
]
