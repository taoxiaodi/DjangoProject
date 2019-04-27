from django.conf.urls import url
from . import views
from .feed import ArticleFeed

app_name = "blogtest"

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^label/(\d+)/$', views.label, name='label'),
    url(r'^classify/(\d)/$', views.classify, name='classify'),
    url(r'^detail/(\d+)/$', views.detail, name='detail'),
    url(r'^pigeonhole/(\d)/$', views.pigeonhole, name='pigeonhole'),
    url(r'^rss/$', ArticleFeed(), name='rss'),
]