# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 14:06:42 2021

@author: YULiu
"""
from django.urls import path
from rango import views
app_name = 'rango'
urlpatterns = [
path('', views.index, name='index'),
path('about/', views.about, name='about'),
]
