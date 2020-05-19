from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template.context_processors import csrf
from registration.models import logindb1
def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    try:
        user = logindb1.objects.get(username=username)
        if user.password == password:
            request.session['username'] = username
            print(request.session['username'])
            return HttpResponseRedirect('/home/enterdata/')
        else:
            return HttpResponseRedirect('/loginmodule/invalidlogin/')
    except logindb1.DoesNotExist:
        return HttpResponseRedirect('/loginmodule/userdoesnotexist')

def loggedin(request):
    return render_to_response('loggedin.html', {"full_name": request.user.username})

def invalidlogin(request):

    return render_to_response('invalidlogin.html')

def logout(request):
    if 'username' in request.session:
        del request.session['username']
        return render_to_response('logout.html')
    else:
        return render_to_response('logout.html')


def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('login.html', c)

def userdoesnotexist(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('userdoesnotexist.html', c)
