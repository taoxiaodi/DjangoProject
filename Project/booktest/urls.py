from django.conf.urls import url
from . import views

app_name = 'booktest'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^list/$', views.list, name='list'),
    url(r'detail/(\d+)/$', views.detail, name='detail'),
    url(r'^delete/(\d+)/$', views.delete, name='delete'),
    url(r'^add/(\d+)/$', views.add, name='add'),
    url(r'^addhero/(\d+)/$', views.addhero, name='addhero'),
    url(r'^addbook/$', views.addbook, name='addbook'),
    url(r'^bookname/$', views.bookname, name='bookname'),
    url(r'^editbook/(\d+)/$', views.editbook, name='editbook'),
    url(r'^editname/(\d+)/$', views.editname, name='editname'),
    url(r'edithero/(\d+)/$', views.edithero, name='edithero'),
    url(r'drophero/(\d+)/$', views.drophero, name='drophero'),
    url(r'^editheroinfo/(\d+)/$', views.editheroinfo, name='editheroinfo')
]
