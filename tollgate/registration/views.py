from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.template.context_processors import csrf
from django.views import generic
from .models import logindb1
from django.shortcuts import render

def getuser(request):
    if 'ausername' in request.session:
        user1 = logindb1.objects.filter()
        con = {'toll': user1,}
        return render(request, 'adduser.html', context=con)
    else:
        return HttpResponseRedirect('/adminuser/login/')


def adduser(request):
    if 'ausername' in request.session:
        uname = request.POST.get('username', '')
        pword = request.POST.get('password', '')
        loc = request.POST.get('location', '')
        lane = request.POST.get('lane', '')
        user = logindb1.objects.filter(username=uname)
        for u in user:
            if u.username == uname:
                msg='Username is already exist'
                con = {'msg': msg, }
                return render(request, 'errors.html', context=con)

        u = logindb1.objects.filter(location=loc)
        if u == None:
            print("yo yo")
        else:
            for i in u:
                if i.lane==lane:
                    msg = 'lane is already exists'
                    user1 = logindb1.objects.filter()
                    con = {'toll': user1,'msg':msg }
                    return render(request, 'errors.html', context=con)
        s = logindb1(username=uname, password=pword, location=loc, lane=lane)
        s.save()
        return HttpResponseRedirect('/registration/addsuccess/')
    else:
        return HttpResponseRedirect('/adminuser/login/')


def deluser(request):
    if 'ausername' in request.session:
        user = logindb1.objects.filter()
        con = {'toll': user, }
        return render(request, 'deluser.html', context=con)
    else:
        return HttpResponseRedirect('/adminuser/login/')



def deleteuser(request):
    if 'ausername' in request.session:
        try:
            uname = request.POST.get('del', '')
            user = logindb1.objects.filter(username=uname)
            for u in user:
                if u.username == uname:
                    user.delete()
                    user = logindb1.objects.filter()
            con = {'toll': user, }
            return render(request, 'deluser.html', context=con)
    #        return render_to_response('delrecord.html')
        except logindb1.DoesNotExist:
            return HttpResponseRedirect('/loginmodule/userdoesnotexist')
    else:
        return HttpResponseRedirect('/adminuser/login/')


def addsuccess(request):
    if 'ausername' in request.session:
        user = logindb1.objects.filter()
        con = {'toll': user, }
        return render(request, 'adduser.html', context=con)
    else:
        return HttpResponseRedirect('/adminuser/login/')


