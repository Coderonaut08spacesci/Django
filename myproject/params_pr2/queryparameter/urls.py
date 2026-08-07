from django.contrib import admin
from django.urls import path
from .import views
urlpatterns=[
    path('setf/',views.setform ,name='setf'),
    path('getf/',views.getform,name='getf'),
    ]