from builtins import type

from django.shortcuts import render_to_response
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.views import generic
from .models import tollgatedb
from update.models import updatedb
from registration.models import logindb1
from django.utils.timezone import utc
import datetime
# from django.db.models import F
from dateutil.relativedelta import relativedelta
from datetime import datetime


def enterdata(request):
    if 'username' in request.session:
        username = request.session['username']
        c = logindb1.objects.get(username=username)
        print (c.location)
        user = tollgatedb.objects.filter(src=c.location)
        con = {'toll': user, }
        return render(request, 'adddata.html', context=con)
    else:
        return HttpResponseRedirect('/loginmodule/login/')


def adddata(request):
    try:

        msg = 'dcd'
        if 'username' in request.session:
            username = request.session['username']
            print(request.session['username'])
            v = request.POST.get('vehicleno', '')
            user = logindb1.objects.get(username=username)
            d = request.POST.get('dest', '')
            ch = request.POST.get('charge', '')
            u = tollgatedb.objects.filter(vehicleno=v).last()
            now = datetime.now()
            print(now)

            if u == None:
                print("yo yo")
            elif u.vehicleno is not None and u.journy == 'return':
                then = datetime(u.date.year, u.date.month, u.date.day, u.date.hour, u.date.minute, u.date.second)
                now1 = datetime(now.year, now.month, now.day, now.hour, now.minute, now.second)
                duration = now1 - then
                if ch == 'RETURN':
                    if duration.total_seconds() / 3600 < 24:
                        s = tollgatedb(vehicleno=v, src=user.location, dest=d, charge=u.charge, vehiclename=u.vehiclename,
                                       journy='DONE')
                        s.save()
                        msg = 'you are returned before 24 hours'
                        print (msg)
                    elif duration.total_seconds() / 3600 > 24:
                        print(msg)
                        msg = 'time out '
                        con = {'msg': msg, }
                        return render(request, 'errors1.html', context=con)

                    else:
                        msg = 'yo are doing wrong'
                        print (msg)
                        con = {'msg': msg, }
                        return render(request, 'errors1.html', context=con)

            elif u.vehicleno is not None and u.journy == 'DONE':
                if ch == 'RETURN':
                    msg = 'vehicle completed its return'
                    print(msg)
                    con = {'msg': msg, }
                    return render(request, 'errors1.html', context=con)


            elif u.vehicleno is not None and u.journy == 'single':
                if ch == 'RETURN':
                    msg = 'vehicle did not take return type'
                    print(msg)
                    con = {'msg': msg, }
                    return render(request, 'errors1.html', context=con)
            charge = 0
            if ch == 'BIKE':
                c = updatedb.objects.get(vehicle=ch)
                s = tollgatedb(vehicleno=v, src=user.location, dest=d, charge=c.amount, vehiclename='BIKE')
                charge=c.amount
                s.save()
            elif ch == 'CAR':
                c = updatedb.objects.get(vehicle=ch)
                s = tollgatedb(vehicleno=v, src=user.location, dest=d, charge=c.amount, vehiclename='CAR')
                charge = c.amount
                s.save()
            elif ch == 'BUS':
                c = updatedb.objects.get(vehicle=ch)
                s = tollgatedb(vehicleno=v, src=user.location, dest=d, charge=c.amount, vehiclename='BUS')
                charge = c.amount
                s.save()
            elif ch == 'BIKE_RET':
                c = updatedb.objects.get(vehicle=ch)
                s = tollgatedb(vehicleno=v, src=user.location, dest=d, charge=c.amount, journy='return', vehiclename='BIKE')
                charge = c.amount
                s.save()
            elif ch == 'CAR_RET':
                c = updatedb.objects.get(vehicle=ch)
                s = tollgatedb(vehicleno=v, src=user.location, dest=d, charge=c.amount, journy='return', vehiclename='CAR')
                charge = c.amount
                s.save()
            elif ch == 'BUS_RET':
                c = updatedb.objects.get(vehicle=ch)
                s = tollgatedb(vehicleno=v, src=user.location, dest=d, charge=c.amount, journy='return', vehiclename='BUS')
                charge = c.amount
                s.save()

            print(user.location)
            user1 = tollgatedb.objects.filter(src=user.location)
            con = {'toll': user1,'vno': v,'dec': d,'chrg': ch,'time':  now,'amount':charge,'name':username,}
            return render(request, 'print.html', context=con)
        else:
            return HttpResponseRedirect('/loginmodule/login/')
    except logindb1.DoesNotExist:
        return HttpResponseRedirect('/loginmodule/login/')



def places(request):
    if 'username' in request.session:
        username = request.session['username']
        print(request.session['username'])
        user = logindb1.objects.get(username=username)
        s = user.location
        user1 = tollgatedb.objects.filter(src=user.location)
        con = {'toll': user1, }
        return render(request, 'places.html', context=con)
    else:
        return HttpResponseRedirect('/loginmodule/login/')


def placecharge(request):
    if 'username' in request.session:
        username = request.session['username']
        print(request.session['username'])
        user = logindb1.objects.get(username=username)
        s = user.location
        d = request.POST.get('dest', '')
        user = tollgatedb.objects.filter(src=s, dest=d)
        j = 0
        for i in user:
            j = j + i.charge;
        con = {'amount': j, 'toll': user, }
        return render(request, 'places1.html', context=con)
    else:
        return HttpResponseRedirect('/loginmodule/login/')


def distdate(request):
    if 'username' in request.session:
        username = request.session['username']
        user = logindb1.objects.get(username=username)
        user1 = tollgatedb.objects.filter(src=user.location)
        con = {'toll': user1, }
        return render(request, 'distdate.html', context=con)
    else:
        return HttpResponseRedirect('/loginmodule/login/')


def info(request):
    if 'username' in request.session:
        return render(request, 'info.html')
    else:
        return HttpResponseRedirect('/loginmodule/login/')




def distdate1(request):
    if 'username' in request.session:
        d = request.POST.get('date', '')
        now = datetime.now()
        da = datetime.strptime(d, '%Y-%m-%dT%H:%M')
        then = datetime(da.year, da.month, da.day, da.hour, da.minute)
        diff = now - then
        sec = diff.total_seconds()
        username = request.session['username']
        user1 = logindb1.objects.get(username=username)
        user = tollgatedb.objects.filter(src=user1.location)
        m = 0
        c = []
        for i in user:
            now1 = datetime(i.date.year, i.date.month, i.date.day, i.date.hour, i.date.minute)
            diff1 = now - now1
            sec1 = diff1.total_seconds()
            if (sec >= sec1):
                c.append(i)
                m = m + i.charge
        con = {'amount': m, 'toll': c, }
        return render(request, 'distdate1.html', context=con)
    else:
        return HttpResponseRedirect('/loginmodule/login/')



def vehicle(request):
    if 'username' in request.session:
        username = request.session['username']
        user = logindb1.objects.get(username=username)

        user1 = tollgatedb.objects.filter(src=user.location)
        con = {'toll': user1, }
        return render(request, 'vehicle.html', context=con)
    else:
        return HttpResponseRedirect('/loginmodule/login/')




def vehicle1(request):
    if 'username' in request.session:
        vh = request.POST.get('charge', '')
        jt = request.POST.get('type', '')
        username = request.session['username']
        user1 = logindb1.objects.get(username=username)

        print(jt)
        print("sdfsac")
        j = 0
        if jt == 'ALL':
            user = tollgatedb.objects.filter(vehiclename=vh, src=user1.location)
            for i in user:
                j = j + i.charge;
                print("sdf")
        else:
            user = tollgatedb.objects.filter(vehiclename=vh, src=user1.location, journy=jt)
            for i in user:
                j = j + i.charge;

        con = {'amount': j, 'toll': user, }
        return render(request, 'vehicle1.html', context=con)
    else:
        return HttpResponseRedirect('/loginmodule/login/')







