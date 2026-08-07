from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [
    path('',views.home1),
    path('menudetails/<int:mid>',views.menudets,name='Menu'),
]