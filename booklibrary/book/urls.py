from django.conf.urls import url
from . import views

app_name = 'book'

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^login/$', views.login, name='login'),
    url(r'^register/$', views.register, name='register'),
    url(r'clear_info/$', views.clear_info, name='clear_info'),
    url(r'^reader_info/(\D+)$', views.reader_info, name='reader_info'),
    url(r'^reader_modify$', views.reader_modify, name='reader_modify'),
    url(r'^reader_save_modify$', views.reader_save_modify, name='reader_save_modify'),
    url(r'^reader_query$', views.reader_query, name='reader_query'),
    url(r'^reader_book/(\d+)$', views.reader_book, name='reader_book'),
    url(r'^reader_history/$', views.reader_history, name='reader_history'),
    url(r'^up_load/$', views.up_load, name='up_load'),
    url(r'^text/(\d+)/$', views.text, name='text'),
    url(r'^edit/$', views.edit, name='edit'),
    url(r'^article_list/$', views.article_list, name='article_list'),
    url(r'^mail/$', views.mail, name='mail'),
    url(r'^active/(.*?)/$', views.active, name='active'),

    # 异步刷新相关视图
    url(r'^ajax/$', views.ajax, name='ajax'),
    url(r'^ajaxajax/$', views.ajaxajax, name='ajaxajax'),
    url(r'^ajaxlogin/$', views.ajaxlogin, name='ajaxlogin'),
    url(r'^verify/$', views.verify, name='verify'),
    url(r'^verifyimg/$', views.verifyimg, name='verifyimg'),

    # echarts
    url(r'echarts', views.echarts, name='echarts')
]
