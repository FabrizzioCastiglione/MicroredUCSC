"""
URL configuration for microreducsc project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from graph.views import  main,index,canal1, canal2, canal3, canal4,canal5,canal6,canal7,canal8,canal9,canal10,canal11,canal12

urlpatterns = [
    path('',index),
    path('main/', main),
     path('canal1/', canal1, name="canal1"),
    path('canal2/', canal2, name="canal2"),
    path('canal3/', canal3, name="canal3"),
    path('canal4/', canal4, name="canal4"),
    path('canal5/', canal5, name="canal5"),
    path('canal6/', canal6, name="canal6"),
    path('canal7/', canal7, name="canal7"),
    path('canal8/', canal8, name="canal8"),
    path('canal9/', canal9, name="canal9"),
    path('canal10/', canal10, name="canal10"),
    path('canal11/', canal11, name="canal11"),
    path('canal12/', canal12, name="canal12"),
]
