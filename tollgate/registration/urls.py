from django.urls import path,include
from django.conf.urls import url

from registration import views

urlpatterns = [
   # path('', views.index, name='index'),
    url(r'adduser/$', views.adduser),
    url(r'deluser/$', views.deluser),
    url(r'getuser/$', views.getuser),
    url(r'addsuccess/$', views.addsuccess),
    url(r'deleteuser/$', views.deleteuser),

]
