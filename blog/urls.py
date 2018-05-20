from django.conf.urls import url
from . import views
from django.shortcuts import render, get_object_or_404
urlpatterns=[
    url(r'^$',views.post_list,name='post_list'),
    url(r'post/(?P<pk>\d+)$',views.post_detail,name='post_detail'),
]