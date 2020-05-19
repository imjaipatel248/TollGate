from builtins import int

from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.template.context_processors import csrf
from django.views import generic
from .models import updatedb

def getvehicle(request):
    if 'ausername' in request.session:
        c = {}
        c.update(csrf(request))
        return render_to_response('update.html', c)
    else:
        return HttpResponseRedirect('/adminuser/login/')


def updatevehicle(request):
    if 'ausername' in request.session:
        bike = request.POST.get('bike','')
        car = request.POST.get('car', '')
        bus = request.POST.get('bus', '')
        bike_ret = request.POST.get('bike_ret', '')
        car_ret = request.POST.get('car_ret', '')
        bus_ret = request.POST.get('bus_ret', '')
        s = updatedb(id=1, vehicle='bike', amount=int(bike))
        s.save()
        s = updatedb(id=2, vehicle='car', amount=int(car))
        s.save()
        s = updatedb(id=3, vehicle='bus', amount=int(bus))
        s.save()
        s = updatedb(id=4, vehicle='bike_ret', amount=int(bike_ret))
        s.save()
        s = updatedb(id=5, vehicle='car_ret', amount=int(car_ret))
        s.save()
        s = updatedb(id=6, vehicle='bus_ret', amount=int(bus_ret))
        s.save()
        return HttpResponseRedirect('/update/updatesuccess/')
    else:
        return HttpResponseRedirect('/adminuser/login/')


def updatesuccess(request):
    if 'ausername' in request.session:
        return render_to_response('success.html')
    else:
        return HttpResponseRedirect('/adminuser/login/')
