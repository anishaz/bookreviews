from django.shortcuts import render, redirect

def index(request):
    return render(request, 'reviews/index.html')

def add(request):
     return render(request, 'reviews/add.html')

def show(request):
     pass
