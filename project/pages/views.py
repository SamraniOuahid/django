from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Article
from .serializers import ArticleSerializer
from django.http import JsonResponse
import json

# Create your views here.

def index(request):
    x={'name':'rachid ouahid',
     'age':1900000348
     }
    return render(request,'pages/index.html',x)

def about(request):
    return render(request,'pages/about.html')

class ArticleListCreateView(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticleDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer