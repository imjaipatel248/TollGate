from datetime import datetime

from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template.context_processors import csrf
from django.forms.fields import DateTimeField
from home.models import tollgatedb
from registration.models import logindb1


def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    try:
        user = auth.authenticate(username=username,
                                 password=password)
        if user is not None:
            request.session['ausername'] = username
            auth.login(request, user)
            return HttpResponseRedirect('/adminuser/loggedin/')
        else:
            return HttpResponseRedirect('/adminuser/invalidlogin/')
    except auth.DoesNotExist:
        return HttpResponseRedirect('/adminuser/invalidlogin/')


def loggedin(request):
    if 'ausername' in request.session:
        user = logindb1.objects.filter()
        con = {'toll': user, }
        return render(request, 'aloggedin.html', context=con)
    else:
        return HttpResponseRedirect('/adminuser/login/')

  #  return render_to_response('aloggedin.html', {"full_name": request.user.username})


def invalidlogin(request):
    return render_to_response('ainvalidlogin.html')


def logout(request):
    if 'ausername' in request.session:
        del request.session['ausername']
        auth.logout(request)
        return render_to_response('alogout.html')
    else:
        return HttpResponseRedirect('/adminuser/login/')


def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('alogin.html', c)


def distcharge(request):
    if 'ausername' in request.session:
        user1 = tollgatedb.objects.filter()
        con = {'toll': user1, }
        return render(request, 'aplaces.html', context=con)
    else:
        return HttpResponseRedirect('/adminuser/login/')


def distamount(request):
    if 'ausername' in request.session:

        d = request.POST.get('dest', '')
        s = request.POST.get('src', '')
        user = tollgatedb.objects.filter(src=s, dest=d)
        j = 0
        for i in user:
            j = j + i.charge;
        con = {'amount': j, 'toll': user, }
        return render(request, 'aplaces1.html', context=con)
    else:
        return HttpResponseRedirect('/adminuser/login/')


def distdate(request):
    if 'ausername' in request.session:
        user1 = tollgatedb.objects.filter()
        con = {'toll': user1, }
        return render(request, 'adistdate.html', context=con)
    else:
        return HttpResponseRedirect('/adminuser/login/')



def distdate1(request):
    if 'ausername' in request.session:
        d = request.POST.get('date', '')
        now=datetime.now()
        da=datetime.strptime(d, '%Y-%m-%dT%H:%M')
        then = datetime(da.year,da.month,da.day,da.hour,da.minute)
        diff=now-then
        sec=diff.total_seconds()
        user = tollgatedb.objects.filter()
        m = 0
        c=[]
        for i in user:
            now1=datetime(i.date.year,i.date.month,i.date.day,i.date.hour,i.date.minute)
            diff1=now-now1
            sec1=diff1.total_seconds()
            if(sec>=sec1):
                c.append(i)
                m=m+i.charge
        con = {'amount':m, 'toll': c, }
        return render(request, 'adistdate1.html', context=con)
    else:
        return HttpResponseRedirect('/adminuser/login/')



def vehicle(request):
    if 'ausername' in request.session:
        user1 = tollgatedb.objects.filter()
        con = {'toll': user1, }
        return render(request, 'avehicle.html', context=con)
    else:
        return HttpResponseRedirect('/adminuser/login/')


def info(request):
    if 'ausername' in request.session:
        return render(request, 'ainfo.html')
    else:
        return HttpResponseRedirect('/adminuser/login/')



def vehicle1(request):
    if 'ausername' in request.session:
        vh = request.POST.get('charge', '')
        jt = request.POST.get('type', '')
        print(jt)
        print("sdfsac")
        j = 0
        if jt=='ALL':
          user = tollgatedb.objects.filter(vehiclename=vh)
          for i in user:
                j = j + i.charge;
                print("sdf")
        else:
            user = tollgatedb.objects.filter(vehiclename=vh,journy=jt)
            for i in user:
                j = j + i.charge;

        con = {'amount': j, 'toll': user, }
        return render(request, 'vehicle1.html', context=con)
    else:
        return HttpResponseRedirect('/adminuser/login/')

