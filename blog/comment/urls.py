from django.conf.urls import url
from . import views

app_name = 'comment'

urlpatterns = [
    url(r'^discuss/(\d+)/$', views.discuss, name='discuss'),
]