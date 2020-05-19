from django.urls import path
from adminuser.views import login, auth_view, logout, loggedin, invalidlogin, distamount, distcharge, distdate, info,distdate1, vehicle1, vehicle
from django.contrib.auth import views as auth_views
from django.conf.urls import url
urlpatterns = [
url(r'^login/$', login),
url(r'^auth/$', auth_view),
url(r'^logout/$', logout),
url(r'^loggedin/$', loggedin),
url(r'^invalidlogin/$', invalidlogin),
url(r'^distcharge/$', distcharge),
url(r'^distamount/$', distamount),
url(r'^distdate/$', distdate),
url(r'^distdate1/$', distdate1),
url(r'^vehicle/$', vehicle ),
url(r'^vehicle1/$', vehicle1),
url(r'^info/$', info),


]