from django.conf.urls import url
from blogapp import views

urlpatterns = [
    url(r'^index/$', views.index, name='index')
]
