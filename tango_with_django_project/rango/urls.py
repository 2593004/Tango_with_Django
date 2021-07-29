# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 14:06:42 2021

@author: YULiu
"""
from django.urls import path
from rango import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'rango'
urlpatterns = [
path('', views.index, name='index'),
path('about/', views.about, name='about'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
