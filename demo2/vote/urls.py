from django.conf.urls import url
from . import views

app_name = 'vote'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^poll/(\d+)/$', views.poll, name='poll'),
    url(r'^detail/(\d+)/$', views.detail, name='detail'),
    url(r'^info/(\d+)/$', views.info, name='info'),
    url(r'^all/$', views.all, name='all'),
    url(r'^add/$', views.add, name='add'),
    url(r'^writeque/$', views.writeque, name='writeque'),
    url(r'^dropque/(\d+)/$', views.dropque, name='dropque'),
    url(r'^edit/(\d+)/$', views.edit, name='edit'),
    url(r'^editsave/(\d+)/$', views.editsave, name='editsave'),
    url(r'^addoption/(\d+)/$', views.addoption, name='addoption'),
    url(r'^writeoption/(\d+)/$', views.writeoption, name='writeoption'),
]
