from home.views import vehicle,vehicle1,adddata,enterdata,placecharge,places,distdate,distdate1,info


from django.conf.urls import url
urlpatterns = [
url(r'adddata/$', adddata),
url(r'enterdata/$', enterdata),
url(r'places/$', places),
url(r'placecharge/$', placecharge),
url(r'^distdate/$', distdate),
url(r'^distdate1/$', distdate1),
url(r'^vehicle/$', vehicle),
url(r'^vehicle1/$', vehicle1),
url(r'^info/$', info),


]