from django.shortcuts import render
from django.http import HttpResponse
from .models import Male, Female
# Create your views here.
def index(request):
    return render(request, 'pages/index.html', {'name':'rachid'})
def pages(request):
    return render(request, 'pages/about.html', {'n1':'ouahid'} )

#{'pro': Male.objects.get(name_male='oussama')}#