from django.conf.urls import url
from . import views
app_name = 'demo1'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^list/$', views.list, name='list'),
    url(r'^login/$', views.login, name='login')
]
