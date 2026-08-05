from django.contrib import admin
from django.urls import path,include
from .import views
urlpatterns=[
    path('',views.setform ,name='setf'),
    path('getf/',views.getform,name='getf'),
    ]