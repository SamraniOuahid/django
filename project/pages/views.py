from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.

def index(request):
    x={'name':'rachid ouahid',
     'age':1900000348
     }
    return render(request,'pages/index.html',x)

def about(request):
    return render(request,'pages/about.html')