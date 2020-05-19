from django.urls import path,include
from django.conf.urls import url

from update import views

urlpatterns = [
   # path('', views.index, name='index'),
    url(r'updatevehicle/', views.updatevehicle),
    url(r'getvehicle/', views.getvehicle),
    url(r'updatesuccess/', views.updatesuccess),
]
