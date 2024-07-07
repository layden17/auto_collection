"""auto_collection URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.urls import path
from auto import views

urlpatterns = [
    path('', views.car_list, name='car_list'),
    path('new/', views.car_create, name='car_create'),
    path('<int:pk>/edit/', views.car_update, name='car_update'),
    path('<int:pk>/delete/', views.car_delete, name='car_delete'),
]
