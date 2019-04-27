from django.conf.urls import url
from . import views


app_name = "article_text.txt"

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^lable/(\d+)/$', views.lable, name='lable'),
    url(r'^classify/(\d)/$', views.classify, name='classify'),
    url(r'^detail/(\d+)/$', views.detail, name='detail'),
    url(r'^pigeonhole/(\d)/$', views.pigeonhole, name='pigeonhole'),
]
