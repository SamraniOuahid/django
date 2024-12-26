from django.urls import path
from . import views
from .views import ArticleListCreateView, ArticleDetailView

urlpatterns=[
    path('', views.index, name='index'),
    path('about',views.about, name='about'),
    path('articles/', ArticleListCreateView.as_view(), name='article-list-create'),
    path('articles/<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
]