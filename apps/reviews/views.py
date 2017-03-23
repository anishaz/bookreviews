from django.shortcuts import render, redirect
from ..loginreg.models import User

def index(request):
    return render(request, 'reviews/index.html')

def add(request):
    x = User.objects.get(id=request.session['user'])
    y = Book.objects.create(title=request.POST['title'], author=request.POST['author'], creator = x)
    Review.objects.create(rating= request.POST['rating'], comment=request.POST['comment'], user = x, book = y)
    return render(request, 'reviews/add.html')

def show(request):
     pass
