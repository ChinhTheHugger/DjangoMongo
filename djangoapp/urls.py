from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('', index),
    path('test', create_book),
    path('find', find_book)
]