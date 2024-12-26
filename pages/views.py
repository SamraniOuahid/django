from django.shortcuts import render
from .models import Male, Login, Female
from django.http import HttpResponse
from .forms import LoginForm
from django.http import JsonResponse
import json
# Create your views here.
def index(request):

    dataLogin = LoginForm(request.POST)
    # dataLogin.save()
    # if request.method == 'POST':
    #     user = request.POST.get('username')
    #     passw = request.POST.get('password')
        
    #     if user and passw:
    #         data = Login(username=user, password=passw)
    #         data.save()
    #         return HttpResponse("Data saved successfully")
    #     else:
    #         return HttpResponse("Please provide both username and password")
    
    return render(request, 'pages/index.html',{'lf':LoginForm()})

def pages(request):
    return render(request, 'pages/about.html', {'n1': 'ouahid'})
def json(request):
    data = list(Female.objects.values())
    return JsonResponse(data, safe=False)
