from django.contrib import admin
from django.urls import path
from .import views
urlpatterns=[
    path('',views.demo ,name='demo'),
    path('get/',views.showdata,name='data'),
    ]