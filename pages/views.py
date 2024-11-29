from django.shortcuts import render
from django.http import HttpResponse
from .models import Male
# Create your views here.
def index(request):
    return HttpResponse('hello to index')
def pages(request):
    return render(request, 'pages/pages.html', {'pro': Male.objects.get(name_male='ouahid')})