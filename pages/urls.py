from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= 'index'),
    path('pages', views.pages, name= 'pages'),
    path('json/', views.json, name= 'json'),
]