from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('',index),
    path('about-us',about_us),
    path('create',create),
]


