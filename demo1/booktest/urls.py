from django.conf.urls import url
from . import views

app_name = 'booktest'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'booklist/$', views.book_list, name='list'),
    url(r'detail/(\d+)/$', views.detail, name='detail')
]