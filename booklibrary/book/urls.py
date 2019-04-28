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
    url(r'reader_query$', views.reader_query, name='reader_query'),
    url(r'reader_book/(\d+)$', views.reader_book, name='reader_book'),
    url(r'reader_history/$', views.reader_history, name='reader_history'),
]
