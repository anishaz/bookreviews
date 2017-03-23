from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages

def index(request):
    return render(request, 'loginreg/index.html')

def register(request):
    result = User.objects.registration(request.POST.copy())

    if 'errors' in result:
        for errors in result['errors']:
            messages.add_message(request, messages.ERROR, errors)
        return redirect('/')

    request.session['user'] = result['user'].first_name
    request.session['action'] = "registered"

    return redirect ('/success')

def login(request):
    result = User.objects.login(request.POST.copy())

    if 'errors' in result:
        for errors in result['errors']:
            messages.add_message(request, messages.ERROR, errors)
        return redirect ('/')

    request.session['user'] = result['user'].first_name
    request.session['action'] = "logged in"

    return redirect('/success')

def success(request):
    if not 'user' in request.session:
        return redirect('/')
    return render(request, 'loginreg/success.html')

def logout(request):
    request.session.clear()
    return redirect('/')
