#from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.homepage),
    path('count/', views.count, name ='count'),
]
