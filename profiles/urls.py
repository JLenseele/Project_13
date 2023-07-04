from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.profiles_index, name='profiles_index'),
    path('<str:username>/', views.profile, name='profile'),
]
