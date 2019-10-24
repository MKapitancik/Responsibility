from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='search'),
    path('index', views.index, name='index'),
    path('search/<str:question>/', views.search, name='question'),    
]