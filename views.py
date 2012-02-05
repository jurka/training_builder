# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login')
def home(request):
    return render_to_response('home.html', locals())


def login_page(request):
    if request.user.is_authenticated():
        print(repr(request))
        return redirect('/')
    else:
        if 'username' in request.POST and 'password' in request.POST:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                message = "Unable to login"
                return render_to_response('login.html', message=message)
        return render_to_response('login.html')


@login_required(login_url='/login')
def logout_page(request):
    logout(request)
    return render_to_response('login.html')
